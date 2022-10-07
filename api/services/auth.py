from datetime import datetime, timedelta
from typing import Optional
import os

from dotenv import load_dotenv
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models.users import User as UserModel
from schemas.token import TokenData
from services.database import get_db


load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
ALGORITHM = os.getenv('ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, username: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.username == str(username)).first()


def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = get_user(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def generate_token(db: Session, username, password):
    user = authenticate_user(db=db, username=username, password=password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email/username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    return create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(db=db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

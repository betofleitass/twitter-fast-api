from datetime import datetime
from typing import List
import uuid


from sqlalchemy.orm import Session

from models.users import User as UserModel
from schemas import UserCreate
from services.auth import oauth2_scheme


# CRUD for Users

def get_user(db: Session, user_id: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.user_id == str(user_id)).first()


def get_user_by_email(db: Session, email: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_username(db: Session, username: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[UserModel]:
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate) -> UserModel:
    db_user: UserModel = UserModel(
        user_id=str(uuid.uuid4()),
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        birth_date=user.birth_date,
        email=user.email,
        hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: str, username: str) -> UserModel:
    user: UserModel = get_user(db, user_id=user_id)
    if user:
        if username:
            user.username = username
        db.commit()
    return user


def delete_user(db: Session, user_id: str) -> UserModel:
    user: UserModel = get_user(db, user_id=user_id)
    if user:
        db.delete(user)
        db.commit()
    return user

from datetime import datetime
import uuid

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate
from .auth import get_password_hash

# CRUD for Users


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == str(user_id)).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        user_id=str(uuid.uuid4()),
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        birth_date=user.birth_date,
        email=user.email,
        hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: str, username: str):
    user = get_user(db, user_id=user_id)
    if user:
        if username:
            user.username = username
        db.commit()
    return user


def delete_user(db: Session, user_id: str):
    user = get_user(db, user_id=user_id)
    if user:
        db.delete(user)
        db.commit()
    return user

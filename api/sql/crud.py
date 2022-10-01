from sqlalchemy.orm import Session

from sql import alchemy_models
from models.models import User, UserCreate
from models.models import Tweet


def get_user(db: Session, user_id: int):
    return db.query(alchemy_models.User).filter(alchemy_models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(alchemy_models.User).filter(alchemy_models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(alchemy_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = alchemy_models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(alchemy_models.Item).offset(skip).limit(limit).all()

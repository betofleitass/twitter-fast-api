import uuid

from sqlalchemy.orm import Session

from sql import alchemy_models
from models.models import User, UserCreate
from models.models import Tweet


def get_user(db: Session, user_id: str):
    return db.query(alchemy_models.User).filter(alchemy_models.User.user_id == str(user_id)).first()


def get_user_by_email(db: Session, email: str):
    return db.query(alchemy_models.User).filter(alchemy_models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(alchemy_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = alchemy_models.User(
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


def post_tweet(db: Session, tweet: Tweet):
    db_tweet = alchemy_models.Tweet(
        tweet_id=str(uuid.uuid4()),
        user_id=str(tweet.user_id),
        text=tweet.text,
        created_time=tweet.created_time,)
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(alchemy_models.Item).offset(skip).limit(limit).all()

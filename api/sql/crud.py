import uuid

from datetime import datetime

from sqlalchemy.orm import Session

from sql import models
from schemas.users import User, UserCreate
from schemas.tweets import Tweet, TweetCreate


# Users

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == str(user_id)).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = models.User(
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


# Tweets

def post_tweet(db: Session, tweet: TweetCreate):
    db_tweet = models.Tweet(
        tweet_id=str(uuid.uuid4()),
        user_id=str(tweet.user_id),
        text=tweet.text,
        created_time=datetime.now(),
    )
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet


def get_tweets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tweet).offset(skip).limit(limit).all()


def get_tweet(db: Session, tweet_id: str):
    return db.query(models.Tweet).filter(models.Tweet.tweet_id == str(tweet_id)).first()


def delete_tweet(db: Session, tweet_id: str):
    tweet = get_tweet(db, tweet_id=tweet_id)
    if tweet:
        db.delete(tweet)
        db.commit()
    return tweet

from datetime import datetime
import uuid

from sqlalchemy.orm import Session

from sql import models
from schemas.tweets import TweetCreate


# CRUD for Tweets

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

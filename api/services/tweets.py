from datetime import datetime
from typing import List
import uuid

from sqlalchemy.orm import Session

from models.tweets import Tweet as TweetModel
from schemas import TweetCreate


# CRUD for Tweets

def post_tweet(db: Session, tweet: TweetCreate) -> TweetModel:
    db_tweet: TweetModel = TweetModel(
        tweet_id=str(uuid.uuid4()),
        user_id=str(tweet.user_id),
        text=tweet.text,
        created_time=datetime.now(),
    )
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet


def get_tweets(db: Session, skip: int = 0, limit: int = 100) -> List[TweetModel]:
    return db.query(TweetModel).offset(skip).limit(limit).all()


def get_tweet(db: Session, tweet_id: str) -> TweetModel:
    return db.query(TweetModel).filter(TweetModel.tweet_id == str(tweet_id)).first()


def delete_tweet(db: Session, tweet_id: str) -> TweetModel:
    tweet = get_tweet(db, tweet_id=tweet_id)
    if tweet:
        db.delete(tweet)
        db.commit()
    return tweet

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship

from .database import Base


# SQLAlchemy models


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    hashed_password = Column(String)

    tweets = relationship("Tweet", back_populates="user",
                          cascade="all, delete-orphan")


class Tweet(Base):
    __tablename__ = "tweets"

    tweet_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id",))
    text = Column(String)
    created_time = Column(DateTime)

    user = relationship("User",
                        back_populates="tweets",)

from sqlalchemy import Column, ForeignKey, String, DateTime, Date
from sqlalchemy.orm import relationship

from config.database import Base


class Tweet(Base):
    __tablename__ = "tweets"

    tweet_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id",))
    text = Column(String)
    created_time = Column(DateTime)

    user = relationship("User",
                        back_populates="tweets",)

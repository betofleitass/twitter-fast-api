from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, Field


class TweetBase(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=280,
        example="This is a tweet"
    )


class TweetCreate(TweetBase):
    user_id: UUID = Field(
        ...,
        title="The user who tweeted it",
        example="4zb48f84-4865-3214-z7qw-6c654e48aga7")


class Tweet(TweetBase):
    tweet_id: UUID = Field(
        ...,
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6")
    created_time: datetime = Field(
        default=datetime.now(),
        title="Date and time when was tweeted",
        example="2021-06-25 07:58:56.550604"
    )

    class Config:
        orm_mode = True

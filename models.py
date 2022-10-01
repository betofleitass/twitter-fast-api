from doctest import Example
from enum import Enum
from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, SecretStr


class BaseUser(BaseModel):
    user_id: UUID = Field(...)
    username: str = Field(
        ...,
        min_length=1,
        max_length=15,
        example="johndoe")
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="John")
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Doe")
    email: EmailStr = Field(
        ...,
        Example="johndoe@gmail.com")
    birth_date: date = Field(
        ...,
        Example="1990-10-30")


class UserIn(BaseUser):
    password: SecretStr = Field(
        ...,
        min_length=8,
        max_length=64)


class UserOut(BaseUser):
    ...


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    user_id: UserIn = Field(...)
    text: str = Field(
        ...,
        min_length=1,
        max_length=280,
        example="This is a tweet"
    )
    created_time: datetime = Field(
        default=datetime.now(),
        example="2021-06-25 07:58:56.550604"
    )

from enum import Enum
from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, SecretStr


class BaseUser(BaseModel):
    user_id: UUID = Field(...)
    username: str = Field(
        ...,
        min_length=1,
        max_length=15)
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50)
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50)
    email: EmailStr = Field(...)
    birth_date: date = Field(...)


class UserIn(BaseUser):
    password: SecretStr = Field(...)


class UserOut(BaseUser):
    ...

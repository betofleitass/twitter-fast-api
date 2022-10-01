# from datetime import date
# from uuid import UUID

# from pydantic import BaseModel, EmailStr, Field, SecretStr

# from models.tweets_model import Tweet


# class UserBase(BaseModel):
#     username: str = Field(
#         ...,
#         min_length=1,
#         max_length=15,
#         example="johndoe")
#     first_name: str = Field(
#         ...,
#         min_length=1,
#         max_length=50,
#         example="John")
#     last_name: str = Field(
#         ...,
#         min_length=1,
#         max_length=50,
#         example="Doe")
#     email: EmailStr = Field(
#         ...,
#         Example="johndoe@gmail.com")
#     birth_date: date = Field(
#         ...,
#         Example="1990-10-30")


# class UserCreate(UserBase):
#     password: SecretStr = Field(
#         ...,
#         min_length=8,
#         max_length=64)


# class User(UserBase):
#     user_id: UUID = Field(
#         ...,
#         example="4zb48f84-4865-3214-z7qw-6c654e48aga7"
#     )
#     tweets: list[Tweet] = []

#     class Config:
#         orm_mode = True

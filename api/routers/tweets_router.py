from typing import List
from uuid import UUID

from fastapi import (APIRouter, Body, HTTPException,
                     Path, Query, status, )

from models.models import UserCreate, User
from models.models import Tweet

router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


# Tweet Post
@router.post(
    path="/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Post a new tweet"
)
async def post_tweet(
    user: User = Body(
        ...,
        examples={
            "normal": {
                "summary": "A user is created",
                "description": "User creation works correctly.",
                "value": {
                    "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "username": "johndoe",
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "user@example.com",
                    "birth_date": "2022-10-01",
                    "password": "mypassword123"
                },
            },
        },
    )
):
    """
    # Creates a new user and save it to the database:

    # Parameters:
    -  ### Request Body parameter :
        - **user: User**: a User model with the following information:
            - **user_id: UUID (required)** -> User's Id
            - **username: str (required)** -> User's username
            - **first_name: str (required)** -> User's first name
            - **last_name: str (required)** -> User's last name
            - **email: EmailStr (required)** -> User's email
            - **birth_date: date (required)** -> User's birth date
            - **password: SecretStr (required)** -> User's password

    # Returns:
    - **user** : The user that was created with all the information

    # Raises:
    - **HTTP 404**: When an error ocurred during the creation
    """

    return user


# Get List of Tweets
@router.get(
    path="/",
    # response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Get a list of tweets"
)
async def get_tweets(

):
    """
    # Get a list of tweets:

    # Parameters:
    -  ### None

    # Returns:
    - **tweets** : A list of tweets

    # Raises:
    - **HTTP 404**: When an error ocurred
    """

    return {"message": "ok"}


# Get a Tweet
@router.get(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Get a tweet"
)
async def get_tweet(
        tweet_id: UUID = Path(
        ...,
        title="Tweet's id",
        description="The id of the tweet to find. (required)",
        examples={
            "normal": {
                "summary": "Get a tweet",
                "description": "Get tweet works correctly.",
                "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            },
        },
        )
):
    """
    # Get a single tweet with the given tweet id:

    # Parameters:
    -  ### Request Path parameter :
        - **tweet_id: UUID (required)** -> tweet's Id

    # Returns:
    - **tweet** : The tweet that was found with it's information

    # Raises:
    - **HTTP 404**: When an error ocurred getting the tweet
    """

    return {"user": tweet_id}


# Delete Tweet
@router.delete(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet"
)
async def delete_tweet(
        tweet_id: UUID = Path(
        ...,
        title="Tweet's id",
        description="The id of the tweet to be deleted. (required)",
        examples={
            "normal": {
                "summary": "A tweet is deleted",
                "description": "Tweet delete works correctly.",
                "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            },
        },
        )
):
    """
    # Deletes a tweet with the given tweet id:

    # Parameters:
    -  ### Request Path parameter :
        - **tweet_id: UUID (required)** -> tweet's Id

    # Returns:
    - **tweet** : The tweet that was deleted with it's information

    # Raises:
    - **HTTP 404**: When an error ocurred during the delete
    """

    return {"user_deleted": tweet_id}

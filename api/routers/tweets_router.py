from typing import List
from uuid import UUID

from fastapi import (APIRouter, Body, Depends, HTTPException,
                     Path, Query, status, )

from models.models import TweetCreate, Tweet

from sqlalchemy.orm import Session

from sql.database import SessionLocal

from sql import crud

router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Tweet Post
@router.post(
    path="/",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a new tweet"
)
async def post_tweet(
    tweet: TweetCreate = Body(
        ...,
        examples={
            "normal": {
                "summary": "A tweet is posted",
                "description": "Tweet creation works correctly.",
                "value": {
                    "user_id": "22a16cfe-3e06-40bb-9043-2fa419262cf2",
                    "text": "This is a tweet",
                },
            },
        },
    ),
    db: Session = Depends(get_db)
):
    """
    # Post a new tweet and save it to the database:

    # Parameters:
    -  ### Request Body parameter :
        - **tweet: TweetCreate**: a TweetCreate model with the following information:
            - **user_id: UserBase (required)** -> User's Id
            - **text: str (required)** -> Tweet's text

    # Returns:
    - **tweet** : The tweet that was post with all the information

    # Raises:
    - **HTTP 404**: When an error ocurred during the creation
    """
    return crud.post_tweet(db=db, tweet=tweet)


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

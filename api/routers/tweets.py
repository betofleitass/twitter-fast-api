from typing import List
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from schemas.tweets import Tweet, TweetCreate
from schemas.users import User
from services.auth import get_current_user
from services.database import get_db
from services.tweets import (delete_tweet as service_delete_tweet,
                             get_tweet as service_get_tweet,
                             get_tweets as service_get_tweets,
                             post_tweet as service_post_tweet)

router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
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
    return service_post_tweet(db=db, tweet=tweet)


# Get List of Tweets
@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Get a list of tweets"
)
async def get_tweets(
    skip: int = Query(
        default=0,
        title="Skip",
        description="Numbers of tweets to skip",
        ge=0,
        example=5,
    ),
    limit: int = Query(
        default=0,
        title="limit",
        description="Limit the numbers of tweets returned",
        ge=0,
        example=5,
    ),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    # Get a list of tweets:

    # Parameters:
    -  ### Query parameters :
        - **skip: int (optional)** -> Numbers of tweets to skip
        - **limit: int (optional)** -> The limit the numbers of tweets returned

    # Returns:
    - **list[Tweet]** : A list of tweets

    # Raises:
    - **HTTP 404**: When an error ocurred
    """

    db_tweets = service_get_tweets(db, skip=skip, limit=limit)
    return db_tweets


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
                "value": "cd5bf8d1-8e70-49b2-a4e5-6c6d37fdd266",
            },
        },
        ),
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
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

    db_tweet = service_get_tweet(db, tweet_id=tweet_id)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return db_tweet


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
        ),
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
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
    db_tweet = service_delete_tweet(db, tweet_id)
    if db_tweet is None:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return db_tweet

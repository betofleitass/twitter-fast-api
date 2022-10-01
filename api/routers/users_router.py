from typing import List
from uuid import UUID

from fastapi import (APIRouter, Body, FastAPI, HTTPException,
                     Path, Query, status, )

from models.users_model import UserIn, UserOut

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# User Create
@router.post(
    path="/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new User",
    tags=["Users"]
)
async def create_user(
    user: UserIn = Body(
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
        - **user: UserIn**: a userIn model with the following information:
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


# List of Users Read
@router.get(
    path="/",
    # response_model=List[UserOut],
    status_code=status.HTTP_200_OK,
    summary="Get a list of users",
    tags=["Users"]
)
async def get_users(

):
    """
    # Get a list of users:

    # Parameters:
    -  ### None

    # Returns:
    - **users** : A list of users

    # Raises:
    - **HTTP 404**: When an error ocurred
    """

    return {"message": "ok"}


# User Read
@router.get(
    path="/{user_id}",
    # response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Get a user",
    tags=["Users"]
)
async def get_user(
        user_id: UUID = Path(
        ...,
        title="User's id",
        description="The id of the user to find. (required)",
        examples={
            "normal": {
                "summary": "Get a user",
                "description": "User get works correctly.",
                "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            },
        },
        )
):
    """
    # Get a single user with the given user id:

    # Parameters:
    -  ### Request Path parameter :
        - **user_id: UUID (required)** -> User's Id

    # Returns:
    - **user** : The user that was found with it's information

    # Raises:
    - **HTTP 404**: When an error ocurred during the update
    """

    return {"user": user_id}

# User Update


@router.put(
    path="/{user_id}",
    # response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
async def update_user(
        user_id: UUID = Path(
        ...,
        title="User's id",
        description="The id of the user to be updated. (required)",
        examples={
            "normal": {
                "summary": "A user is updated",
                "description": "User update works correctly.",
                "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            },
        },
        )
):
    """
    # Updates a user with the given user id:

    # Parameters:
    -  ### Request Path parameter :
        - **user_id: UUID (required)** -> User's Id

    # Returns:
    - **user** : The user that was updated with it's information

    # Raises:
    - **HTTP 404**: When an error ocurred during the update
    """

    return {"user_updated": user_id}


# User Delete
@router.delete(
    path="/{user_id}",
    # response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
async def delete_user(
        user_id: UUID = Path(
        ...,
        title="User's id",
        description="The id of the user to be deleted. (required)",
        examples={
            "normal": {
                "summary": "A user is deleted",
                "description": "User delete works correctly.",
                "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            },
        },
        )
):
    """
    # Deletes a user with the given user id:

    # Parameters:
    -  ### Request Path parameter :
        - **user_id: UUID (required)** -> User's Id

    # Returns:
    - **user** : The user that was deleted with it's information

    # Raises:
    - **HTTP 404**: When an error ocurred during the update
    """

    return {"user_deleted": user_id}

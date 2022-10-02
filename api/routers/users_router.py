from typing import List, Optional
from uuid import UUID

from fastapi import (APIRouter, Body, Depends, HTTPException,
                     Path, Query, status)
from sqlalchemy.orm import Session

from schemas.users import UserCreate, User
import services.users as service
from sql.database import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# User Create
@router.post(
    path="/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new User"
)
async def create_user(
    user: UserCreate = Body(
        ...,
        examples={
            "normal": {
                "summary": "A user is created",
                "description": "User creation works correctly.",
                "value": {
                    "username": "johndoe",
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "user@example.com",
                    "birth_date": "2022-10-01",
                    "password": "mypassword123"
                },
            },
        },
    ),
    db: Session = Depends(get_db)
):
    """
    # Creates a new user and save it to the database:

    # Parameters:
    -  ### Request Body parameter :
        - **user: UserCreate**: a UserCreate model with the following information:
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

    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db=db, user=user)


# List of Users Read
@router.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Get a list of users"
)
async def get_users(
    skip: int = Query(
        default=0,
        title="Skip",
        description="Numbers of users to skip",
        ge=0,
        example=5,
    ),
    limit: int = Query(
        default=0,
        title="limit",
        description="Limit the numbers of users returned",
        ge=0,
        example=5,
    ),
    db: Session = Depends(get_db)
):
    """
    # Get a list of users:

    # Parameters:
    -  ### Query parameters :
        - **skip: int (optional)** -> Numbers of users to skip
        - **limit: int (optional)** -> The limit the numbers of users returned

    # Returns:
    - **list[User]** : A list of users

    # Raises:
    - **HTTP 404**: When an error ocurred
    """

    db_users = service.get_users(db, skip=skip, limit=limit)
    return db_users


# User Read
@router.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get a user"
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
                "value": "3fa85f64-5717-4562-b3fc-2c963f66afa3",
            },
        },
        ),
        db: Session = Depends(get_db)
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

    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# User Update
@router.put(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user"
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
        ),
        username: Optional[str] = Query(
            None,
            title="New username",
            description="Updates the username",
            min_length=4,
            max_length=15,
            example="newusername",
        ),
        db: Session = Depends(get_db)
):
    """
    # Updates a user with the given user id:

    # Parameters:
    -  ### Request Path parameter :
        - **user_id: UUID (required)** -> User's Id

    -  ### Query parameter :
        - **username: str (optional)** -> New username

    # Returns:
    - **user** : The user that was updated with it's information

    # Raises:
    - **HTTP 404**: When an error ocurred during the update
    """

    # Chekc if the user exists
    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the username is taken
    db_user_username = service.get_user_by_username(db, username=username)
    if db_user_username:
        raise HTTPException(status_code=404, detail="Username already taken")

    # If no exception is raised
    db_user = service.update_user(db,
                                  user_id=user_id,
                                  username=username)

    return db_user


# User Delete
@router.delete(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user"
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
        ),
        db: Session = Depends(get_db)
):
    """
    # Deletes a user with the given user id:

    # Parameters:
    -  ### Request Path parameter :
        - **user_id: UUID (required)** -> User's Id

    # Returns:
    - **user** : The user that was deleted with it's information

    # Raises:
    - **HTTP 404**: When an error ocurred during the delete
    """

    db_user = service.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

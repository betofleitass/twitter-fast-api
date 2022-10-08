from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas.token import Token
from schemas.users import User, UserCreate
from services.auth import generate_token, get_current_user, get_password_hash
from services.database import get_db
from services.users import (get_user_by_email as service_get_user_by_email,
                            get_user_by_username as service_get_user_by_username,
                            create_user as service_create_user)


router = APIRouter(
    tags=["Authentication"],
)


# Sing up
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Signup"
)
async def sing_up(
    user: UserCreate = Body(
        ...,
        examples={
            "normal": {
                "summary": "User signup",
                "description": "Signup works correctly.",
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
) -> User:
    """
    # Register a new user and save it to the database:

    # Parameters:
    -  ### Request Body parameter:
        - **user: UserCreate** -> a UserCreate model with the following information:
            - **username: str (required)** -> User's username
            - **first_name: str (required)** -> User's first name
            - **last_name: str (required)** -> User's last name
            - **email: EmailStr (required)** -> User's email
            - **birth_date: date (required)** -> User's birth date in (YYYY-MM-DD) format. Eg: (2022-10-01)
            - **password: SecretStr (required)** -> User's password

    # Returns:
    - **user: User** : The registered user with its information

    # Raises:
    - **HTTP 400**: The email or username is already registered
    - **HTTP 422**: Validation error
    """
    # Check email
    db_user = service_get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Check username
    db_user = service_get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    # Hash the password
    user.password = get_password_hash(password=user.password)
    return service_create_user(db=db, user=user)


# Login
@router.post(
    path="/login",
    response_model=Token,
    status_code=status.HTTP_200_OK,
    summary="Login for access token"
)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
) -> Token:
    """
    # Login for access token:

    # Parameters:
    -  ### Request Body parameter :
        - **form_data: Form**: a Form with the following information:
            - **username: str (required)** -> User's username
            - **password: str (required)** -> User's password

    # Returns:
    - **Token** : The access token and it's type

    # Raises:
    - **HTTP 401**: Incorrect username or password
    - **HTTP 422**: Validation error
    """
    access_token = generate_token(
        db=db,
        username=form_data.username,
        password=form_data.password)
    return Token(access_token=access_token, token_type="bearer")


# Current user information
@router.get(
    path="/me",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get current logged in user")
async def me(current_user: User = Depends(get_current_user)) -> User:
    """
    # Get information of the current logged in user:

    # Returns:
    - **current_user**: User -> The current logged in user information

    # Raises:
    - **HTTP 401**: User is not authenticated
    - **HTTP 401**: Could not validate credentials
    - **HTTP 422**: Validation error
    """
    return current_user

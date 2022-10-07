from typing import List, Optional
from uuid import UUID

from fastapi import (APIRouter, Body, Depends, HTTPException,
                     Path, Query, status)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config import SessionLocal
from schemas import UserCreate, User
from schemas.token import Token
from services import users as service
from services.database import get_db
from services.auth import oauth2_scheme, generate_token, get_current_user

router = APIRouter(
    tags=["Token"],
)


@router.get("/items/")
async def read_items(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    return {"token": token}


@router.post(
    "/login",
    response_model=Token
)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)):
    """
    ## Login for access token
    ### Args
    The app can recive next fields by form data
    - username: Your username or email
    - password: Your password
    ### Returns
    - access token and token type
    """
    access_token = generate_token(
        db=db,
        username=form_data.username,
        password=form_data.password)
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

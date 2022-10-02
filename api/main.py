from fastapi import (Body, FastAPI, HTTPException,
                     Path, Query, status, )

from pydantic import EmailStr, SecretStr
from sql import alchemy_models

from routers import users_router, tweets_router

from sqlalchemy.orm import Session

import models

from sql.database import SessionLocal, engine

alchemy_models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users_router.router)
app.include_router(tweets_router.router)


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"])
async def home():
    return {"Hello": "World"}

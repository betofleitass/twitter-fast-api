from fastapi import (Body, FastAPI, HTTPException,
                     Path, Query, status, )

from pydantic import EmailStr, SecretStr

from routers import users_router


app = FastAPI()


app.include_router(users_router.router)


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"])
async def home():
    return {"Hello": "World"}

# Users

# Tweets
# Tweet Create
# Tweet Read
# Tweet Update
# Tweet Delete

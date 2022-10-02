from fastapi import (FastAPI, status)


from routers import users_router, tweets_router

from sql import models
from sql.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users_router.router)
app.include_router(tweets_router.router)


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"])
async def home():
    return {"Hello": "World"}

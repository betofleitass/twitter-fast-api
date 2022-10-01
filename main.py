from typing import Optional

from fastapi import (Body, FastAPI, HTTPException,
                     Path, Query, status, )

from pydantic import EmailStr, SecretStr

import models

app = FastAPI()


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"])
async def home():
    return {"Hello": "World"}

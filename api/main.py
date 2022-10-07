from fastapi import (FastAPI, status)
from fastapi.openapi.utils import get_openapi


from config.database import Base
from config.database import engine
from routers.users import router as user_router
from routers.token import router as token_router
from routers.tweets import router as tweets_router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(token_router)
app.include_router(user_router)
app.include_router(tweets_router)


# Customize open api schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Twitter API",
        version="1.0",
        description=""" ### This is a Twitter API project. You can create, read, update and delete Users and Tweets.
        \n  - ## [Project's repository on GitHub](https://github.com/betofleitass/twitter-fast-api/)
        \n  - ## [Contact me](https://www.linkedin.com/in/fleitas-alberto/)""",
        routes=app.routes,
        license_info={"name": "License: MIT",
                      "url": "https://choosealicense.com/licenses/mit/"}
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


from config.database import Base
from config.database import engine
from api.routers.users import router as user_router
from api.routers.login import router as token_router
from api.routers.tweets import router as tweets_router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(token_router, prefix="/api/v1",)
app.include_router(user_router, prefix="/api/v1",)
app.include_router(tweets_router, prefix="/api/v1",)


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

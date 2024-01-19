from fastapi import FastAPI
from . import models
from .database import engine
from .router import routers

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(routers.api_router)

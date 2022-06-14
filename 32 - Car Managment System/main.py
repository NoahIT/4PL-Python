# noinspection PyUnresolvedReferences
from fastapi import FastAPI
from database import engine
from routers import user_routers, car_routers
import models

app = FastAPI()

app.include_router(user_routers.router)
app.include_router(car_routers.router)
#more... router reik

models.Base.metadata.create_all(engine)
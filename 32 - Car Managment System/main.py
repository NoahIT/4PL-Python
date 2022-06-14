from fastapi import FastAPI
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from routers import user_routers, car_routers
import models
from datetime import date
today = date.today()

app = FastAPI()

app.include_router(user_routers.router, car_routers.router)

models.Base.metadata.create_all(bind=engine)

#TESTING
#
# session = Session()
# session.add_all([
#    models.User(name = 'Komal Pande', last_name = 'Koti', email = 'komal@gmail.com',password='supersecret'),
#    models.User(name = 'Rajender Nath', last_name = 'Gurgaon', email = 'nath@gmail.com',password='supersecret'),
#    models.User(name = 'S.M.Krishna', last_name = 'Peth, Pune', email = 'smk@gmail.com',password='supersecret'),
#    models.Car(brand='Audi', model='A6', consumption='12', mileage='230000', price='5344', cratedAT=today)]
# )
# session.commit()
# noinspection PyUnresolvedReferences
from sqlalchemy.orm import Session
# noinspection PyUnresolvedReferences
import models

def get_all_cars(db: Session):
    return db.query(models.Car).all()
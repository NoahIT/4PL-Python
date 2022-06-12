from sqlalchemy.orm import Session
import models

def get_all_cars(db: Session):
    return db.query(models.Car).all()
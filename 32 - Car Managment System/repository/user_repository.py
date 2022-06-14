# noinspection PyUnresolvedReferences
from sqlalchemy.orm import Session
# noinspection PyUnresolvedReferences
import models

def get_all_users(db: Session):
    return db.query(models.User).all()
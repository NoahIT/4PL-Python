# noinspection PyUnresolvedReferences
from sqlalchemy.orm import Session
# noinspection PyUnresolvedReferences
import models

def get_all_assigns(db: Session):
    return db.query(models.Assign).all()
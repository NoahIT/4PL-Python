from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def get_all_users(db: Session):
    return db.query(models.User).all()

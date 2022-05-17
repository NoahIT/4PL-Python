from fastapi import APIRouter, Depends, status, HttPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from Repository import user_reporitory
import models
import schemas

router = APIRouter(
    prefix='/api/users',
    tags=["Users"]
)

user = db.query(models.User).filter(models.User.id == id).first()


@router.get('', response_model=List[schemas.HumanShortGetInfoSchema])
def all(db: Session = Depends(get_db)):
    return user_reporitory.get_all_users(db)

@router.get('/{id}', response_model=schemas.HumanShortGetInfoSchema)
def get_single_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

    return user


@router.put('/update/{id}')
def update(id: int, request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user.first():
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User ith id {id} not found"
        )

    user.update(request.dict())
    db.commit()

    return user.first()


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user.first():
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User ith id {id} not found"
        )

    user.delete()
    db.commit()

    return {"details": "Success"}

@router.post('')
def create(request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from repository import user_repository
import models
import schemas


router = APIRouter(
    prefix='/api/users',
    tags=["Users"]
)

user = db.query(models.User).filter(models.User.id == id).first()

#-----------------------------------------------------------------------Returns All Users Info

@router.get('', response_model=List[schemas.UserGetInfoSchema])
def all(db: Session = Depends(get_db)):
    return user_repository.get_all_users(db)

#------------------------------------------------------------------Returns All User Info By ID

@router.get('/{id}', response_model=schemas.UserGetInfoSchema)
def get_single_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

    return user

#-------------------------------------------------------------Updates Selected User Info By ID

@router.put('/update/{id}')
def update(id: int, request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User ith id {id} not found"
        )

    user.update(request.dict())
    db.commit()

    return user.first()

#-------------------------------------------------------------Deletes Selected User Info By ID

@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User ith id {id} not found"
        )

    user.delete()
    db.commit()

    return {"details": "Success"}

#---------------------------------------------------------------------------------Creates User

@router.post('')
def create(request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    new_user = models.User(
        id=request.id,
        public_key=request.public_key,
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=request.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
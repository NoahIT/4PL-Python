# noinspection PyUnresolvedReferences
from fastapi import APIRouter, Depends, status, HTTPException
# noinspection PyUnresolvedReferences
from sqlalchemy.orm import Session
# noinspection PyUnresolvedReferences
from database import get_db
# noinspection PyUnresolvedReferences
from typing import List
# noinspection PyUnresolvedReferences
from repository import assign_repository
# noinspection PyUnresolvedReferences
import models
# noinspection PyUnresolvedReferences
from schemas import assign_schemas, user_schemas, car_schemas


router = APIRouter(prefix='/api/assigned',tags=["Assigned_Users"])

#-----------------------------------------------------------------------Returns All Assigns Info

@router.get('', response_model=List[assign_schemas.AssignGetInfoSchema])
def all(db: Session = Depends(get_db)):
    return assign_repository.get_all_assigns(db)

#------------------------------------------------------------------Returns All Assign Info By ID

@router.get('/{id}', response_model=assign_schemas.AssignGetInfoSchema)
def get_single_by_id(id: int, db: Session = Depends(get_db)):
    assign = db.query(models.Assign).filter(models.Assign.id == id).first()

    if not assign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assign with id {id} not found"
        )

    return assign

#-------------------------------------------------------------Updates Selected Assign Info By ID

@router.put('/update/{id}')
def update(id: int, request: assign_schemas.AssignPostSchema, db: Session = Depends(get_db)):
    assign = db.query(models.Assign).filter(models.Assign.id == id).first()

    if not assign.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assign ith id {id} not found"
        )

    assign.update(request.dict())
    db.commit()

    return assign.first()

#-------------------------------------------------------------Deletes Selected Assign Info By ID

@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    assign = db.query(models.Assign).filter(models.Assign.id == id).first()

    if not assign.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assign ith id {id} not found"
        )

    assign.delete()
    db.commit()

    return {"details": "Success"}

#---------------------------------------------------------------------------------Creates Assign

@router.post('')
def create(request: assign_schemas.AssignPostSchema, db: Session = Depends(get_db)):
    new_assign = models.Assign(
        first_name=user_schemas.UserPostSchema.first_name,
        last_name=user_schemas.UserPostSchema.last_name,
        email=user_schemas.UserPostSchema.email,
        brand=car_schemas.CarPostSchema.Brand,
        model=car_schemas.CarPostSchema.Model
    )

    db.add(new_assign)
    db.commit()
    db.refresh(new_assign)

    return new_assign
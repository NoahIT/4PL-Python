from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from repository import car_repository
import models
import schemas


router = APIRouter(
    prefix='/api/cars',
    tags=["Cars"]
)

car = db.query(models.Car).filter(models.Car.id == id).first()

#------------------------------------------------------------------------Returns All Cars Info

@router.get('', response_model=List[schemas.CarGetInfoSchema])
def all(db: Session = Depends(get_db)):
    return car_repository.get_all_cars(db)

#--------------------------------------------------------------Returns Selected Car Info By ID

@router.get('/{id}', response_model=schemas.CarGetInfoSchema)
def get_single_by_id(id: int, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == id).first()

    if not car:
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )

    return car

#--------------------------------------------------------------Updates Selected Car Info By ID

@router.put('/update/{id}')
def update(id: int, request: schemas.CarPostSchema, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == id).first()

    if not car.first():
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )

    car.update(request.dict())
    db.commit()

    return car.first()

#--------------------------------------------------------------Deletes Selected Car Info By ID

@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == id).first()

    if not car.first():
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )

    car.delete()
    db.commit()

    return {"details": "Success"}

#----------------------------------------------------------------------------------Creates Car

@router.post('')
def create(request: schemas.CarPostSchema, db: Session = Depends(get_db)):
    new_car = models.Car(
        id=request.id,
        public_key=request.public_key,
        brand=request.brand,
        model=request.model,
        consumption=request.consumption,
        mileage=request.mileage,
        price=request.price,
        createdAT=request.createdAT
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car
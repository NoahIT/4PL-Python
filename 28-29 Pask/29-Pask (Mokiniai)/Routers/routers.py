from fastapi import APIRouter, Depends, status, HttPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(
    prefix='/api/students',
    tags=["Students"]
)

@router.get('', response_model=schemas.IndividualGradeSchema)
def get_students_avg_grade(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

    return student

@router.post('')
def create(request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    new_user = models.Student(
        first_name=request.first_name,
        last_name=request.last_name,
        grade=request.grade,
        avg_grade=request.avg_grade
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.put('/update/{id}')
def update(id: int, request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()

    if not student.first():
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User ith id {id} not found"
        )

    student.update(request.dict())
    db.commit()

    return student.first()

@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()

    if not student.first():
        raise HttPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User ith id {id} not found"
        )

    student.delete()
    db.commit()

    return {"details": "Success"}
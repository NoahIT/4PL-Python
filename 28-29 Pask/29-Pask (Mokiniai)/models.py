from database import Base
from sqlalchemy import Column, Integer, String


class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    grade = Column(Integer)
    avg_grade = Column(Integer)

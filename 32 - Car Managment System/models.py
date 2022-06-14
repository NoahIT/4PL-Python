# noinspection PyUnresolvedReferences
from database import Base
# noinspection PyUnresolvedReferences
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, nullable=False)
    #public_key = Column(String(20), index=True, nullable=False, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

class Car(Base):
    __tablename__ = "Car"

    id = Column(Integer, primary_key=True, nullable=False)
    #public_key = Column(String(20), index=True, nullable=False, unique=True)
    brand = Column(String)
    model = Column(String)
    consumption = Column(Integer)
    mileage = Column(Integer)
    price = Column(Integer)
    createdAT = Column(Integer)

class Assign(Base):
    __tablename__ = "Assigned_Users"

    id = Column(Integer, primary_key=True, nullable=False)
    #public_key = Column(String(20), index=True, nullable=False, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    brand = Column(String)
    model = Column(String)

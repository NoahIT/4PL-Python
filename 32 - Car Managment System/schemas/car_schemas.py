# noinspection PyUnresolvedReferences
from pydantic import BaseModel, constr

class CarGetInfoSchema(BaseModel): # To Get
    # id: int
    Brand: str
    Model: str
    Price: str
    Consumption: float
    Mileage: float
    CreatedAT:int

class CarPostSchema(BaseModel): # To create
    # id: int
    Brand: str
    Model: str
    Price: str
    Consumption: float
    Mileage: float
    CreatedAT: int

    class Config:
        orm_mode = True



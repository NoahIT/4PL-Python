# noinspection PyUnresolvedReferences
from pydantic import BaseModel, constr
import user_schemas, car_schemas

class AssignPostSchema(BaseModel): # To Create
    #UserINF:
    first_name: user_schemas.UserPostSchema.first_name
    last_name: user_schemas.UserPostSchema.last_name
    email: user_schemas.UserPostSchema.email
    #CarINF:
    brand: car_schemas.CarPostSchema.Brand
    model: car_schemas.CarPostSchema.Model

    class Config:
        orm_mode = True

class AssignGetInfoSchema(BaseModel): # To Get
    # UserINF:
    first_name: user_schemas.UserPostSchema.first_name
    last_name: user_schemas.UserPostSchema.last_name
    email: user_schemas.UserPostSchema.email
    # CarINF:
    brand: car_schemas.CarPostSchema.Brand
    model: car_schemas.CarPostSchema.Model

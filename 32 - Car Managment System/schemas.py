from pydantic import BaseModel, constr, EmailStr


class UserGetInfoSchema(BaseModel):
    id: int
    public_key: constr(max_length=20)
    first_name: str
    last_name: str
    email: str

    # class Config:
    #     orm_mode = True

class UserPostSchema(BaseModel):
    id: int
    public_key: constr(max_length=20)
    first_name: str
    last_name: str
    email: str
    password: str

class CarGetInfoSchema(BaseModel):
    id: int
    Brand: str
    Model: str
    Price: str
    Consumption: float
    Mileage: float
    CreatedAT:int

    # class Config:
    #     orm_mode = True

class CarPostSchema(BaseModel):
    id: int
    Brand: str
    Model: str
    Price: str
    Consumption: float
    Mileage: float
    CreatedAT: int

class UserIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    public_key: constr(max_length=20)

    # class Config:
    #     orm_mode = True


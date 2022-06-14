# noinspection PyUnresolvedReferences
from pydantic import BaseModel, constr, EmailStr

class UserGetInfoSchema(BaseModel): #To Get
    # id: int
    first_name: str
    last_name: str
    email: EmailStr

class UserPostSchema(BaseModel): #To Create
    # id: int
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode = True
from pydantic import BaseModel

class HumanLongGetInfoSchema(BaseModel):
    first_name : str
    last_name : str
    email : str
    phone_number : int

    class config:
        orm_mode = True

class HumanShortGetInfoSchema(BaseModel):
    first_name : str
    last_name : str

    class config:
        orm_mode = True

class UserPostSchema(BaseModel):
    first_name : str
    last_name : str
    email : str



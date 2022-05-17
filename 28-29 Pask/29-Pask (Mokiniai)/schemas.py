from pydantic import BaseModel

class IndividualGradeSchema(BaseModel):
    first_name: str
    last_name: str
    grade: int
    avg_grade: int

    class Config:
        orm_mode = True

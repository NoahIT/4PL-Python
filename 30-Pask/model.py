from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

#Set ORM TABLE

Base = declarative_base()

class CompanyOrm(Base):
    __tablename__ = 'Car Companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=70)

    class Config:
        orm_mode = True
        #Set any string max length to 100
        max_anystr_length = 100
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }


co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
)
print(co_orm)
#> <models_orm_mode.CompanyOrm object at 0x7f48594a0e20>
co_model = CompanyModel.from_orm(co_orm)
print(co_model)
#> id=123 public_key='foobar' name='Testing' domains=['example.com',
#> 'foobar.com']
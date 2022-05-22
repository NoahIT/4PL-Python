from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter(
    prefix='/api/users',
    tags=["Users"]
)


patients = [{"person_name": "Adomas"},
            {"person_name": "Saulius'"},
            {"person_name": "Martynas"}]

@app.get("/persons/")
async def read_item(skip: int = 0, limit: int = 10):
    return patients[skip : skip + limit]
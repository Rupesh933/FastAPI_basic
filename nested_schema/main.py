from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    state: str
    country: str
    pin_code: int

class Student(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/student")
def create_student(student: Student):
    return student
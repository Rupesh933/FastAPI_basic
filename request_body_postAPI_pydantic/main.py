from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user(name: str, age: int):
    return {
        "message": "User created successfully",
        "name": name,
        "age": age
    }

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/items")
def create_items(user: User):
    return user


# Optional fields
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    course: Optional[str] = None
    contact: Optional[int] = None
    city: str

@app.post("/students")
def create_student(student: Student):
    return student
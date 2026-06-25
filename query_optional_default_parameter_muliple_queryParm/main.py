from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items(name: str):
    return {
        "name": name
    }

@app.get("/users")
def get_user(name: str = None):
    return {
        "name": name,
        "age": 20
    }

@app.get("/search")
def search(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id):
    return {
        "user_id": user_id
    }

@app.get("/item/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id
    }
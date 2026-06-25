from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message": "Welcome to FastAPI",
        "success": True,
        "statuscode": 200
    }
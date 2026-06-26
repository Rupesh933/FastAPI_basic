from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    complete: bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"TODO Added",
        "todo": todo
    }

@app.get("/todos")
def get_todo():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {
                "message": "todo find successfully",
                "todo": todo
            }
    return {"error": "Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, update_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return {
                "message": "Update successfully",
                "todo" : update_todo
            }
    return {
        "error": "Todo not found"
    }

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todo.pop(index)
            return{
                "message": "Todo deleted succssfully",
                "todo": delete_todo
            }
    return {
        "error": "Todo not found"
    }
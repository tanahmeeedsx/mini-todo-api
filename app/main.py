from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Todo(BaseModel):
    id: int
    title: str
    done: bool = False


# in-memory "database" — simple list, resets every restart
todos: list[Todo] = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Mini Todo API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos", status_code=201)
def add_todo(title: str, done: bool = False):
    global next_id
    todo = Todo(id=next_id, title=title, done=done)
    todos.append(todo)
    next_id += 1
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}

    raise HTTPException(status_code=404, detail="Todo not found")

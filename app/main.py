from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mini Todo API")


class Todo(BaseModel):
    id: int
    title: str
    done: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


# In-memory database — resets every restart
todos: list[Todo] = []
next_id = 1


@app.get("/")
def root():
    return {
        "message": "Mini Todo API is running",
        "docs": "/docs",
        "deployment": "automated"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos", status_code=201)
def add_todo(title: str, done: bool = False):
    global next_id

    todo = Todo(
        id=next_id,
        title=title,
        done=done
    )

    todos.append(todo)
    next_id += 1

    return todo


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, update: TodoUpdate):
    for todo in todos:
        if todo.id == todo_id:
            if update.title is not None:
                todo.title = update.title

            if update.done is not None:
                todo.done = update.done

            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}

    raise HTTPException(status_code=404, detail="Todo not found")

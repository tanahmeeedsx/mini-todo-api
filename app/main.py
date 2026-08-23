from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mini Todo API")


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


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str | None = None, done: bool | None = None):
    for todo in todos:
        if todo.id == todo_id:
            if title is not None:
                todo.title = title
            if done is not None:
                todo.done = done
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(i)
    raise HTTPException(status_code=404, detail="Todo not found")

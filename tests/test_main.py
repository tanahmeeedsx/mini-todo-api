from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_and_get_todo():
    response = client.post("/todos", params={"title": "Buy milk"})
    assert response.status_code == 201
    assert response.json()["title"] == "Buy milk"

    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_delete_nonexistent_todo():
    response = client.delete("/todos/9999")
    assert response.status_code == 404

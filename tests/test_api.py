from fastapi.testclient import TestClient

from main import app
from routers import items, users

client = TestClient(app)


def reset_in_memory_stores() -> None:
    users.users_db.clear()
    users.next_user_id = 1
    items.items_db.clear()
    items.next_item_id = 1


def test_root_endpoint() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI project is running"}


def test_users_crud_flow() -> None:
    reset_in_memory_stores()

    create_payload = {"name": "Alice", "email": "alice@example.com"}
    create_response = client.post("/users/", json=create_payload)
    assert create_response.status_code == 201
    created_user = create_response.json()
    assert created_user["id"] == 1

    list_response = client.get("/users/")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    get_response = client.get("/users/1")
    assert get_response.status_code == 200
    assert get_response.json()["email"] == "alice@example.com"

    update_payload = {"name": "Alice Updated", "email": "alice.updated@example.com"}
    update_response = client.put("/users/1", json=update_payload)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Alice Updated"

    delete_response = client.delete("/users/1")
    assert delete_response.status_code == 204

    missing_response = client.get("/users/1")
    assert missing_response.status_code == 404


def test_items_crud_flow() -> None:
    reset_in_memory_stores()

    create_payload = {
        "name": "Laptop",
        "description": "14-inch ultrabook",
        "price": 999.99,
    }
    create_response = client.post("/items/", json=create_payload)
    assert create_response.status_code == 201
    created_item = create_response.json()
    assert created_item["id"] == 1

    list_response = client.get("/items/")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    get_response = client.get("/items/1")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Laptop"

    update_payload = {
        "name": "Laptop Pro",
        "description": "16-inch ultrabook",
        "price": 1299.99,
    }
    update_response = client.put("/items/1", json=update_payload)
    assert update_response.status_code == 200
    assert update_response.json()["price"] == 1299.99

    delete_response = client.delete("/items/1")
    assert delete_response.status_code == 204

    missing_response = client.get("/items/1")
    assert missing_response.status_code == 404

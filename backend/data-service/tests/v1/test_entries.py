from fastapi.testclient import TestClient


def test_list_entries(categories_entries, client: TestClient):
    response = client.get("/archive/entries/")
    assert response.status_code == 200
    assert len(response.json()) == 4


def test_list_category_entries(categories_entries, client: TestClient):
    response = client.get("/archive/categories/1/entries")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == [
        {"category_id": 1, "id": 1, "name": "Pirmasens", "visible_to_player": True},
        {"category_id": 1, "id": 2, "name": "Berlin", "visible_to_player": True},
    ]


def test_list_category_entries_no_exist(categories_entries, client: TestClient):
    response = client.get("/archive/categories/1111/entries")
    assert response.status_code == 404
    assert len(response.json()) == 1
    assert response.json() == {"detail": "Category not found"}


def test_list_entry(categories_entries, client: TestClient):
    response = client.get("/archive/entries/1")
    assert response.status_code == 200
    assert len(response.json()) == 4
    assert response.json() == {"category_id": 1, "id": 1, "name": "Pirmasens", "visible_to_player": True}


def test_list_entry_no_exist(categories_entries, client: TestClient):
    response = client.get("/archive/entries/111")
    assert response.status_code == 404
    assert len(response.json()) == 1
    assert response.json() == {"detail": "Entry not found"}


def test_delete_entry(categories_entries, client: TestClient):
    response = client.request(method="DELETE", url="/archive/entries/1")
    assert response.status_code == 204


def test_delete_entry_no_exist(categories_entries, client: TestClient):
    response = client.request(method="DELETE", url="/archive/entries/1111")
    assert response.status_code == 404


def test_update_entry(categories_entries, client: TestClient):
    response = client.put("/archive/entries/1", json={"category_id": 1, "name": "lol", "visible_to_player": False})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "category_id": 1, "name": "lol", "visible_to_player": False}


def test_update_entry_no_exist(categories_entries, client: TestClient):
    response = client.put("/archive/entries/1111", json={"category_id": 1, "name": "lol", "visible_to_player": False})
    assert response.status_code == 404
    assert response.json() == {"detail": "Entry not found"}

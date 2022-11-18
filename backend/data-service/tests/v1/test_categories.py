from v1.crud.archive import get_categories
from fastapi.testclient import TestClient


def test_create_categories(db, client: TestClient):
    response = client.post("/archive/categories/", json={"name": "monster"})
    assert response.status_code == 201
    response = client.post("/archive/categories/", json={"name": "weapon"})
    assert response.status_code == 201

    db_categories = get_categories(db=db)
    assert len(db_categories) == 2


def test_list_categories(categories, client: TestClient):
    response = client.get("/archive/categories/")
    assert len(response.json()) == 2


def test_list_category(categories, client: TestClient):
    response = client.get("/archive/categories/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "place"}


def test_list_category_no_exist(categories, client: TestClient):
    response = client.get("/archive/categories/111")
    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}


def test_create_category_already_exist(categories, client: TestClient):
    response = client.post("/archive/categories/", json={"name": "place"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Category already exists"}


def test_create_category(categories, client: TestClient):
    response = client.post("/archive/categories/", json={"name": "testcat"})
    assert response.status_code == 201
    assert response.json() == {"id": 3, "name": "testcat"}


def test_delete_category_by_id(categories, client: TestClient):
    response = client.delete("/archive/categories/1")
    assert response.status_code == 204


def test_delete_category_by_id_no_exist(categories, client: TestClient):
    response = client.delete("/archive/categories/111")
    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}


def test_delete_category_by_name(categories, client: TestClient):
    response = client.request(method="DELETE", url="/archive/categories/", json={"name": "place"})
    assert response.status_code == 204


def test_delete_category_by_name_no_exist(categories, client: TestClient):
    response = client.request(method="DELETE", url="/archive/categories/", json={"name": "honnebombel"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}


def test_update_category(categories, client: TestClient):
    response = client.put("/archive/categories/1", json={"name": "newplace"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "newplace"}


def test_update_category_no_exist(categories, client: TestClient):
    response = client.put("/archive/categories/111", json={"name": "newplace"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}
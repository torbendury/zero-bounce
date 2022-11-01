from fastapi.testclient import TestClient

from .main import app
from .mock import archive, character

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"error": "Not found"}


def test_read_categories():
    response = client.get("/archive/categories")
    assert response.status_code == 200
    assert response.json() == {"categories": archive.mock_categories}


def test_read_category():
    response = client.get("/archive/categories/1")
    assert response.status_code == 200
    assert response.json() == archive.mock_categories[1]


def test_read_category_no_exist():
    response = client.get("/archive/categories/42")
    assert response.status_code == 404
    assert response.json() == {"error": "The specified category id does not exist"}


def test_read_category_entry():
    response = client.get("/archive/categories/1/entries/0")
    assert response.status_code == 200
    assert response.json() == archive.mock_categories[1]["data"][0]


def test_read_category_entry_category_no_exist():
    response = client.get("/archive/categories/42/entries/0")
    assert response.status_code == 404
    assert response.json() == {
        "error": "The specified category or entry id does not exist"
    }


def test_read_category_entry_entry_no_exist():
    response = client.get("/archive/categories/1/entries/42")
    assert response.status_code == 404
    assert response.json() == {
        "error": "The specified category or entry id does not exist"
    }


def test_read_character():
    response = client.get("/character")
    assert response.status_code == 200
    assert response.json() == {"character": character.mock_character}

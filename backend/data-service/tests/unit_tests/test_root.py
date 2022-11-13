from fastapi.testclient import TestClient

from src.main import app
from src.crud import archive, character

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"error": "Not found"}

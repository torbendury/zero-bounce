from fastapi.testclient import TestClient
import pytest


def test_get_entry_post(client: TestClient):
    response = client.get("/archive/categories/1/entries/1/post")
    assert response.status_code == 200
    assert response.json() == {}
    pytest.fail("Reading entry posts from NoSQL not yet implemented.")

from fastapi.testclient import TestClient


def test_redirect_root_to_docs(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200

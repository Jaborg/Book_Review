from fastapi.testclient import TestClient
import application

client = TestClient(application)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Welcome to the Frontpage!" in response.text
from fastapi.testclient import TestClient
from application import application

client = TestClient(application)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Introspection is a tool to carve out serenity" in response.text

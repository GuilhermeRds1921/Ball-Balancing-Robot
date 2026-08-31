from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_position():

    response = client.get("/position")

    assert response.status_code == 200

    data = response.json()

    assert "x" in data
    assert "y" in data

    assert isinstance(data["x"], int)
    assert isinstance(data["y"], int)
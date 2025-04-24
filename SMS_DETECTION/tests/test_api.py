from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"message": "Free entry in 2 a wkly comp!"})
    assert response.status_code == 200
    assert response.json()["prediction"] in ["Spam", "Ham"]

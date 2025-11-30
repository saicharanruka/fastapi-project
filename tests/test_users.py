from fastapi.testclient import TestClient
from app.api import app


client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json().get("message") == "Welcome to my API"

def test_create_user():
    res = client.post('/users/', json={'email' : 'hello1234@gmail.com', 'password' : 'password'})
    assert res.status_code == 201
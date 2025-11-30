from .database import client, session

def test_root(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json().get("message") == "Welcome to my API"

def test_create_user(client):
    res = client.post('/users/', json={'email' : 'hello1234@gmail.com', 'password' : 'password'})
    assert res.status_code == 201
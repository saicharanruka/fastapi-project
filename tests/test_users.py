import pytest
from app import schemas
from fastapi import status


# def test_root(client):
#     res = client.get("/")
#     assert res.status_code == 200
#     assert res.json().get("message") == "Welcome to my API"

def test_create_user(client):
    res = client.post('/users/', json={'email' : 'hello1234@gmail.com', 'password' : 'password'})
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post('/login', data={'username' : test_user['email'], 'password' : test_user['password']})
    login_res = schemas.Token(**res.json())
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', status.HTTP_403_FORBIDDEN),
    ('sanjeev@gmail.com', 'wrongpassword', status.HTTP_403_FORBIDDEN),
    ('wrongemail@gmail.com', 'wrongpassword', status.HTTP_403_FORBIDDEN),
    # (None, 'password123', 422),
    # ('sanjeev@gmail.com', None, status.HTTP_422_UNPROCESSABLE_CONTENT)

])
def test_incorrect_login(client, email, password, status_code):
    res = client.post('/login', data={'username' : email, 'password' : password})

    print(res.json())
    assert res.status_code == status_code
    # assert res.json().get('detail').lower() == 'Invalid Credentials'.lower()
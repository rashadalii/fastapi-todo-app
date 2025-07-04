from fastapi import status

def test_register(client):
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "password": "password123"
    }
    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.json()
    assert response.json()["username"] == "johndoe"

def test_register_existing_username(client, test_user):
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "username": "testuser",  # already exists
        "password": "password123"
    }
    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_login(client, test_user):
    login_data = {
        "username": "testuser",
        "password": "testpass"
    }
    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

def test_login_invalid_credentials(client, test_user):
    login_data = {
        "username": "testuser",
        "password": "wrongpassword"
    }
    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_refresh_token(client, test_user_token):
    refresh_token = test_user_token["refresh_token"]
    response = client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

def test_refresh_token_invalid(client):
    response = client.post("/api/v1/auth/refresh", json={"refresh_token": "invalid"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
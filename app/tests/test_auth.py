import uuid


def test_register_user(client):
    unique_email = f"user_{uuid.uuid4().hex}@example.com"

    response = client.post(
        "/auth/register",
        json={
            "email": unique_email,
            "password": "Secure@123",
            "role": "customer",
        },
    )

    assert response.status_code == 200
    assert response.json()["message"] == "User registered"


def test_login_user(client):
    email = f"user_{uuid.uuid4().hex}@example.com"

    # register first
    client.post(
        "/auth/register",
        json={
            "email": email,
            "password": "Secure@123",
            "role": "customer",
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": email,
            "password": "Secure@123",
            "role": "customer",
        },
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

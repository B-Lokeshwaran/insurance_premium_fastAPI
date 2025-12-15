def test_create_policy(client):
    response = client.post(
        "/policies/",
        json={
            "name": "Health Insurance",
            "base_amount": 10000,
            "risk_factor": 1.2,
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Health Insurance"


def test_list_policies(client):
    response = client.get("/policies/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_make_payment(client):
    response = client.post(
        "/payments/",
        json={
            "policy_id": 1,
            "amount": 14400,
        },
    )
    assert response.status_code == 200
    assert response.json()["status"] == "SUCCESS"

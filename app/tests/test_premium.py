def test_calculate_premium(client):
    response = client.get(
        "/premium/calculate",
        params={
            "base_amount": 10000,
            "age": 50,
            "risk_factor": 1.2,
        },
    )
    assert response.status_code == 200
    assert "premium" in response.json()

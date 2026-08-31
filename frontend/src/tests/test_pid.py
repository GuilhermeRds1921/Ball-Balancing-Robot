def test_send_pid():

    payload = {
        "kp": 10,
        "ki": 5,
        "kd": 2
    }

    response = client.post(
        "/pid",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "PID atualizado"

    assert data["data"]["kp"] == 10
    assert data["data"]["ki"] == 5
    assert data["data"]["kd"] == 2
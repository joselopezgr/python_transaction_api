import pytest
from flask.testing import FlaskClient

def test_happy_path_event_api(client: FlaskClient):
    event_data = {
        "type": "deposit",
        "amount": "150",
        "time": 10,
        "user_id": 1
    }
    
    response = client.post("/event", json=event_data)
    assert response.status_code == 200
    assert response.json == {
        "alert": False,
        "alert_codes": [],
        "user_id": 1
    }
    
def test_unhappy_path_event_api(client: FlaskClient):
    event_data = {
        "type": "wrong_type",
        "amount": "150",
        "time": 10,
        "user_id": 1
    }
    
    response = client.post("/event", json=event_data)
    assert response.status_code == 400
    assert "error" in response.json
    assert isinstance(response.json["error"], list)
    assert len(response.json["error"]) > 0
    assert "ctx" in response.json["error"][0]
    assert response.json["error"][0]["ctx"] == {
        "expected": "'deposit' or 'withdrawal'"
    }
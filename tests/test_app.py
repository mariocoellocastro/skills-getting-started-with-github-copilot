from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_duplicate_signup_is_rejected():
    response = client.post("/activities/Chess Club/signup?email=student@example.com")
    assert response.status_code == 200

    duplicate_response = client.post("/activities/Chess Club/signup?email=student@example.com")
    assert duplicate_response.status_code == 409


def test_participant_can_be_removed():
    client.post("/activities/Programming Class/signup?email=remove@example.com")

    response = client.delete("/activities/Programming Class/signup?email=remove@example.com")

    assert response.status_code == 200
    assert "Removed" in response.json()["message"]

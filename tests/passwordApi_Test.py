import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.models.PasswordRequest import PasswordRequest
from app.utility.validate_password import validate_password_request

app = FastAPI()

# Import your router and add it to the app
from app.api.passwordApi import router

app.include_router(router)

client = TestClient(app)


def test_generate_password_valid_input():
    request_data = {
        "length": 12,
        "uppercase": True,
        "digits": True,
        "special": False,
    }

    response = client.post("/generate_password", json=request_data)

    assert response.status_code == 200
    assert "password" in response.json()
    assert validate_password_request(PasswordRequest(**request_data)) is None


def test_generate_password_invalid_input():
    request_data = {
        "length": 0,  # Invalid length
        "uppercase": True,
        "digits": True,
        "special": False,
    }

    response = client.post("/generate_password", json=request_data)

    assert response.status_code == 422
    assert "Invalid input" in response.json()["detail"]
    assert "password" not in response.json()


def test_generate_password_exception():
    with pytest.raises(Exception):
        validate_password_request(length=10, uppercase=True, digits=True, special=True)

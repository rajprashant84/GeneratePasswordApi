# app/validation/password_generator.py
from fastapi import HTTPException
from app.models.PasswordRequest import PasswordRequest


def validate_password_request(request: PasswordRequest):
    if not isinstance(request.length, int) or request.length < 1:
        raise HTTPException(status_code=422,
                            detail="Invalid input,Expected length should be a positive integer number.")

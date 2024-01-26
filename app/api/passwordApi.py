# app/api.py
from fastapi import APIRouter, HTTPException, Body
from app.models.PasswordRequest import PasswordRequest
from app.models.PasswordResponse import PasswordResponse
from app.utility.password_generator import password_generate
from app.utility.validate_password import validate_password_request


router = APIRouter()


@router.post("/generate_password", response_model=PasswordResponse, status_code=200)
async def generate_password_endpoint(password_request: PasswordRequest = Body(...)):
    try:
        # Input validation
        validate_password_request(password_request)

        password = password_generate(
            length=password_request.length,
            uppercase=password_request.uppercase,
            digits=password_request.digits,
            special=password_request.special
        )
        return {"password": password}
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


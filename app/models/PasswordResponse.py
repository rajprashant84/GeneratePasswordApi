# app/Response/PasswordResponse.py
from pydantic import BaseModel


class PasswordResponse(BaseModel):
    password: str

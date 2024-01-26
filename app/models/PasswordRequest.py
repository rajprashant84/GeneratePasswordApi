# app/Request/PasswordRequest.py
from pydantic import BaseModel


class PasswordRequest(BaseModel):
    length: int
    uppercase: bool
    digits: bool
    special: bool

# main.py
from fastapi import FastAPI
from app.api.passwordApi import router as api_router

app = FastAPI()

# Include the router in the main app
app.include_router(api_router)
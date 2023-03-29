from fastapi import APIRouter
from fastapi.api.routes import api_router

app = APIRouter()

app.include_router(api_router, prefix="/api/v1/", tags=["app"])

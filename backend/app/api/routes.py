from fastapi import APIRouter
from app.api.endpoints.StudentController import studentroutes

api_router = APIRouter()
api_router.include_router(studentroutes, prefix="/student", tags=["student"])

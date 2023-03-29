from fastapi import APIRouter, status
from fastapi.responses import Response

studentroutes = APIRouter()
studentService = StudentService()


@studentroutes.post("/")
def create_student():
    pass

@studentroutes.get("/{id}")
def get_student():
    pass

@studentroutes.put("/{id}")
def update_student():
    pass

@studentroutes.delete("/{id}")
def delete_student():
    pass


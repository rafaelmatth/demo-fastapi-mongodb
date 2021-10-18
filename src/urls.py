from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

router = APIRouter()

from database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)

from models import (
    error_response_model,
    response_model,
    StudentSchema,
    UpdateStudentModel,
)

@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return response_model(new_student, "Student added successfully.")


from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import sessionmaker, Session
from session.session import get_db
from models.student_response import StudentResponse
from models.student_create import StudentCreate
from models.student_update import StudentUpdate
from service.student_service import StudentService

router = APIRouter()

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return StudentService.get_student(student_id, db)

@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return StudentService.create_student(student, db)

@router.delete("/students/{student_id}", response_model=StudentResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return StudentService.delete_student(student_id, db)

@router.patch("/students/{student_id}", response_model=StudentResponse)
def patch_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    return StudentService.patch_student(student_id, student, db)

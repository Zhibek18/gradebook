from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import sessionmaker, Session
from models.student import Student
from session.session import get_db
from models.student_response import StudentResponse
from models.student_create import StudentCreate
from models.student_update import StudentUpdate

router = APIRouter()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, grade=student.grade)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/students/{student_id}", response_model=StudentResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return db_student

@router.patch("/students/{student_id}", response_model=StudentResponse)
def patch_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Apply partial modifications
    for attr, value in student.dict(exclude_unset=True).items():
        setattr(db_student, attr, value)

    db.commit()
    db.refresh(db_student)
    return db_student

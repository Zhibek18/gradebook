from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from data.student import Student
from models.student_update import StudentUpdate
from models.student_create import StudentCreate
from session.session import (get_db)
from repository.student_repository import StudentRepository

repo = StudentRepository()

class StudentService:
    def get_student(student_id: int, db: Session = Depends(get_db)) -> Student:
        db_student = repo.find(student_id, db)
        return db_student

    def create_student(student: StudentCreate, db: Session = Depends(get_db)) -> Student:
        db_student = Student(name=student.name, surname=student.surname)
        return repo.add(db_student, db)

    def delete_student(student_id: int, db: Session = Depends(get_db)) -> Student:
        return repo.delete(student_id, db)

    def patch_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)) -> Student:
        return repo.update(student_id, student, db)

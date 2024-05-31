from data.student import Student
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from session.session import (get_db)

class StudentRepository:
    def find (self, student_id: int, db: Session = Depends(get_db)) -> Student:
        db_student = db.query(Student).filter(Student.id == student_id).first()
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return db_student

    def add (self, student: Student, db: Session = Depends(get_db)) -> Student:

        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    def delete (self, student_id:int, db: Session = Depends(get_db)) -> Student:
        student = self.find(student_id,db)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        db.delete(student)
        db.commit()
        return student


    def update (self, student_id:int, student: Student, db: Session = Depends(get_db())) -> Student:
        db_student = self.find(student_id, db)
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        for attr, value in student.dict(exclude_unset=True).items():
            setattr(db_student, attr, value)

        db.commit()
        db.refresh(db_student)
        return db_student


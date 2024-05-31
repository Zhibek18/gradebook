from pydantic import BaseModel
from datetime import date

class ScoreCreate(BaseModel):
    student_id: int
    score: int
    date: date
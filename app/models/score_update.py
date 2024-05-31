from pydantic import BaseModel
from datetime import date

class ScoreUpdate(BaseModel):
    student_id: int = None
    score: int = None
    date: date = None
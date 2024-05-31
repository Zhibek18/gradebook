from pydantic import BaseModel
from datetime import date

class ScoreResponse(BaseModel):
    id: int
    student_id: int
    score: int
    date: date
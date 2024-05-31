from pydantic import BaseModel

class StudentResponse(BaseModel):
    id: int
    name: str
    grade: int

from pydantic import BaseModel

class StudentUpdate(BaseModel):
    name: str = None
    grade: int = None

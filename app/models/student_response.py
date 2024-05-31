from pydantic import BaseModel

class StudentResponse(BaseModel):
    id: int
    name: str
    surname: str

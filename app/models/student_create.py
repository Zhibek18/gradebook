from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    surname: str
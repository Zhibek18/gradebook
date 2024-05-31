from pydantic import BaseModel

class StudentUpdate(BaseModel):
    name: str = None
    surname: str = None

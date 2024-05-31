from fastapi import FastAPI
from routers import students


app = FastAPI()

app.include_router(students.router, prefix="/api/v1")
# name surname
# student_id score date  /subject



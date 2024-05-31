from fastapi import FastAPI
from routers import students, scores

app = FastAPI()

app.include_router(students.router, prefix="/api/v1")
app.include_router(scores.router, prefix="/api/v1")

# name surname
# student_id score date  /subject



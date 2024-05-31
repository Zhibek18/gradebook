from fastapi import FastAPI
from sqlalchemy import create_engine
from routers.students import router
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "sqlite:///./grade-book.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api/v1")
# name surname
# student_id score date  /subject



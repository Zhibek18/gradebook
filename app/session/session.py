from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.student import StudentBase
from data.score import ScoreBase

SQLALCHEMY_DATABASE_URL = "sqlite:///./gradebook.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

StudentBase.metadata.create_all(bind=engine)
ScoreBase.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
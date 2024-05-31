from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

ScoreBase = declarative_base()

class Score(ScoreBase):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    score = Column(Integer)
    date = Column(Date)
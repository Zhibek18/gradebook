from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from data.score import Score
from models.score_update import ScoreUpdate
from models.score_create import ScoreCreate
from session.session import (get_db)
from repository.score_repository import ScoreRepository

repo = ScoreRepository()

class ScoreService:
    def get_score(score_id: int, db: Session = Depends(get_db)) -> Score:
        db_score = repo.find(score_id, db)
        return db_score

    def create_score(score: ScoreCreate, db: Session = Depends(get_db)) -> Score:
        db_score = Score(student_id=score.student_id, score = score.score, date=score.date)
        return repo.add(db_score, db)

    def delete_score(score_id: int, db: Session = Depends(get_db)) -> Score:
        return repo.delete(score_id, db)

    def patch_score(score_id: int, score: ScoreUpdate, db: Session = Depends(get_db)) -> Score:
        return repo.update(score_id, score, db)

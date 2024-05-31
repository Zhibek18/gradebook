from data.score import Score
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from session.session import (get_db)

class ScoreRepository:
    def find (self, score_id: int, db: Session = Depends(get_db)) -> Score:
        db_score = db.query(Score).filter(Score.id == score_id).first()
        if db_score is None:
            raise HTTPException(status_code=404, detail="Score not found")
        return db_score

    def add (self, score: Score, db: Session = Depends(get_db)) -> Score:

        db.add(score)
        db.commit()
        db.refresh(score)
        return score

    def delete (self, score_id:int, db: Session = Depends(get_db)) -> Score:
        score = self.find(score_id,db)
        if score is None:
            raise HTTPException(status_code=404, detail="Score not found")
        db.delete(score)
        db.commit()
        return score


    def update (self, score_id:int, score: Score, db: Session = Depends(get_db())) -> Score:
        db_score = self.find(score_id, db)
        if db_score is None:
            raise HTTPException(status_code=404, detail="Score not found")
        for attr, value in score.dict(exclude_unset=True).items():
            setattr(db_score, attr, value)

        db.commit()
        db.refresh(db_score)
        return db_score


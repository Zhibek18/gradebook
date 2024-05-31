from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import sessionmaker, Session
from session.session import get_db
from models.score_response import ScoreResponse
from models.score_create import ScoreCreate
from models.score_update import ScoreUpdate
from service.score_service import ScoreService

router = APIRouter()

@router.get("/scores/{score_id}", response_model=ScoreResponse)
def get_score(score_id: int, db: Session = Depends(get_db)):
    return ScoreService.get_score(score_id, db)

@router.post("/scores/", response_model=ScoreResponse)
def create_score(score: ScoreCreate, db: Session = Depends(get_db)):
    return ScoreService.create_score(score, db)

@router.delete("/scores/{score_id}", response_model=ScoreResponse)
def delete_score(score_id: int, db: Session = Depends(get_db)):
    return ScoreService.delete_score(score_id, db)

@router.patch("/scores/{score_id}", response_model=ScoreResponse)
def patch_score(score_id: int, score: ScoreUpdate, db: Session = Depends(get_db)):
    return ScoreService.patch_score(score_id, score, db)

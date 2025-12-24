from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Skill

router = APIRouter()

@router.get("/", summary="Liste des compétences")
def get_skills(db: Session = Depends(get_db)):
    skills = db.query(Skill).all()
    return [{"id": s.id, "skill": s.skill, "job_reference": s.job_reference} for s in skills]

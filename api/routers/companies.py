from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Company

router = APIRouter()

@router.get("/", summary="Liste des entreprises")
def get_companies(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à ignorer"),
    limit: int = Query(10, ge=1, le=100, description="Nombre maximum d'éléments à retourner"),
    db: Session = Depends(get_db)
):
    companies = (
        db.query(Company)
        .order_by(Company.id)  # Obligatoire pour MSSQL
        .offset(skip)
        .limit(limit)
        .all()
    )
    return [{"id": c.id, "name": c.name} for c in companies]

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Location

router = APIRouter()

@router.get("/", summary="Liste des localisations")
def get_locations(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à ignorer"),
    limit: int = Query(10, ge=1, le=100, description="Nombre maximum d'éléments"),
    db: Session = Depends(get_db)
):
    locations = (
        db.query(Location)
        .order_by(Location.id)  # OBLIGATOIRE pour MSSQL
        .offset(skip)
        .limit(limit)
        .all()
    )

    return [
        {
            "id": loc.id,
            "city": loc.city,
            "country_code": loc.country_code,
            "latitude": loc.latitude,
            "longitude": loc.longitude
        }
        for loc in locations
    ]

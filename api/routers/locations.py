from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Location

router = APIRouter()

@router.get("/", summary="Liste des localisations")
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(Location).all()
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

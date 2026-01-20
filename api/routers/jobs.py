from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Job, Company, Location
from api.auth import get_current_user

router = APIRouter()

@router.get("/jobs/")
def get_jobs(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à ignorer"),
    limit: int = Query(10, ge=1, le=100, description="Nombre maximum d'éléments à retourner"),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)  # 🔐 PROTECTION ICI
):
    jobs = (
        db.query(Job)
        .order_by(Job.job_reference)
        .offset(skip)
        .limit(limit)
        .all()
    )

    results = []
    for job in jobs:
        results.append({
            "job_reference": job.job_reference,
            "wttj_reference": job.wttj_reference,
            "poste": job.poste,
            "remote": job.remote,
            "url": job.url,
            "education_level": job.education_level,
            "profile": job.profile,
            "salary_min": job.salary_min,
            "salary_max": job.salary_max,
            "salary_currency": job.salary_currency,
            "salary_period": job.salary_period,
            "published_at": job.published_at,
            "updated_at": job.updated_at,
            "profession": job.profession,
            "contract_type": job.contract_type,
            "contract_duration_min": job.contract_duration_min,
            "contract_duration_max": job.contract_duration_max,
            "recruitment_process": job.recruitment_process,
            "cover_letter": job.cover_letter,
            "resume": job.resume,
            "portfolio": job.portfolio,
            "picture": job.picture,
            "company_name": job.company.name if job.company else None,
            "location_city": job.location.city if job.location else None,
        })
    return results

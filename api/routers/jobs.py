from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Job, Company, Location

router = APIRouter()

@router.get("/jobs/")
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
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

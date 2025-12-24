from fastapi import FastAPI
from api.routers import jobs, companies, locations, skills

app = FastAPI(title="WTTJ API", version="1.0.0")

# Inclusion des routes
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(companies.router, prefix="/companies", tags=["Companies"])
app.include_router(locations.router, prefix="/locations", tags=["Locations"])
app.include_router(skills.router, prefix="/skills", tags=["Skills"])

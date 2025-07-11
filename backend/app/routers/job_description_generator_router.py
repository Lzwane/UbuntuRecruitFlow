from app.schemas import schemas
from app.utils.cohere_client import generate_job_description
from fastapi import APIRouter,HTTPException

router = APIRouter()

'''
    endpoint for generating the job discription
    return dictionary(json) job title, location, work type, generated job description

'''
@router.post("/generate-jd")
def generate_job_description_endpoint(data: schemas.JobInput):
    try:
        description = generate_job_description(data.dict())
        return {
            "job_title": data.job_title,
            "location": data.location,
            "work_type": data.work_type,
            "generated_description": description
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {e}")
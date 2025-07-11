from fastapi import APIRouter,Response, status,Depends
from app.schemas import schemas
from app.models.job_post_model import Job
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

'''
    end point for storing the job details
'''

@router.post("/jobs", response_model=schemas.JobSaveInput)
def save_job(data: schemas.JobSaveInput, db: Session = Depends(get_db)):
    job = Job(
        job_title=data.job_title,
        location=data.location,
        work_type=data.work_type,
        generated_description=data.generated_description,
        user_id=data.user_id,
    )
    db.add(job)
    db.commit()
    db.refresh(job)

    return Response(status_code=status.HTTP_201_CREATED)

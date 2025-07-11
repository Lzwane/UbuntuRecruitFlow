from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cv_model import CV
from app.models.job_post_model import Job
from app.models.application_model import Application
from app.schemas.schemas import CVCreate
from app.utils.cohere_client import analyze_cv_match  # your cohere logic

router = APIRouter()

@router.post("/cv/submit")
def submit_cv(data: CVCreate, db: Session = Depends(get_db)):
    # checking if the job exists
    job = db.query(Job).filter(Job.id == data.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found.")

    # 2. Creating a CV record
    new_cv = CV(**data.dict())
    db.add(new_cv)
    db.commit()
    db.refresh(new_cv)
    
    
    # Analyzing CV using Cohere
    analysis = analyze_cv_match(data.dict(), job.generated_description)

    # Storing application with match score & feedback
    application = Application(
        cv_id=new_cv.id,
        job_id=data.job_id,
        #user_id=data.user_id,
        match_score=analysis["rating"],
        feedback=analysis["feedback"]
    )
    db.add(application)
    db.commit()

    return {
        "message": "CV submitted and analyzed successfully.",
        "application_feedback": analysis
    }

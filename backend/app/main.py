from fastapi import FastAPI,HTTPException
from app.routers import testrouter,job_router,job_description_generator_router,cv_route,application_route
from app.database import engine, Base
from app.models import job_post_model, user_model,cv_model,application_model
from pydantic import BaseModel
from typing import List, Optional



app = FastAPI()

Base.metadata.create_all(bind=engine)  # Create tables 

app.include_router(testrouter.router)
app.include_router(job_router.router)
app.include_router(job_description_generator_router.router)
app.include_router(cv_route.router)
app.include_router(application_route.router)





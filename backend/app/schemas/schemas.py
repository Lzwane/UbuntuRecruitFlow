from pydantic import BaseModel
from typing import List, Optional,Any,Dict

class JobInput(BaseModel):
    job_title: str
    role_summary: str
    key_responsibilities: List[str]
    required_skills: List[str]
    preferred_skills: Optional[List[str]] = None
    min_experience_years: int
    max_experience_years: int
    location: str
    work_type: str

class JobSaveInput(BaseModel):
    job_title: str
    location: str
    work_type: str
    generated_description: str
    user_id: int

class Message(BaseModel):
    message: str

class CVCreate(BaseModel):
    name: str
    surname: str
    address: str
    email: str
    cell_number: str
    industry_interest: str
    interests: List[str]
    skills: List[str]
    projects: List[str]
    experience: List[dict]
    education: List[dict]
    job_id: int
    #user_id: int

class CVOut(BaseModel):
    name: str
    surname: str
    skills: List[str]
    address: str
    email: str
    cell_number: str
    industry_interest: str
    interests: List[str]
    experience: List[Dict[str, Any]]
    education: List[Dict[str, Any]]

class ApplicationOut(BaseModel):
    id: int
    cv_id: int
    job_id: int
    match_score: float
    feedback: str
    cv: CVOut


    
    class Config:
        orm_mode = True



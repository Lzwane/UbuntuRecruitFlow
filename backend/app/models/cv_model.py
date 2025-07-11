from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class CV(Base):
    __tablename__ = "cvs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    name = Column(String)
    surname = Column(String)
    address = Column(String)
    email = Column(String)
    cell_number = Column(String)
    industry_interest = Column(String)
    interests = Column(JSON)
    skills = Column(JSON)
    projects = Column(JSON)
    experience = Column(JSON)  
    education = Column(JSON)   

    job = relationship("Job", back_populates="cvs")
    applications = relationship("Application", back_populates="cv")

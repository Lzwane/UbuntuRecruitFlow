from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Application(Base):
    __tablename__ = "applications"
   
    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("cvs.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    #user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    match_score = Column(Float, nullable=True)
    feedback = Column(Text)

    cv = relationship("CV", back_populates="applications")
    job = relationship("Job", back_populates="applications")
    #user = relationship("User", back_populates="applications")

from sqlalchemy.orm import Session
from app.models.analysis import Analysis
from app.models.resume import Resume
from app.core.ai import analyze_resume
from fastapi import HTTPException

def create_analysis(resume_id: int, job_description: str, user_id: int, db: Session):
    resume = db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    if not resume.extracted_text:
        raise HTTPException(status_code=400, detail="Resume has no extracted text")
    
    ai_result = analyze_resume(resume.extracted_text, job_description)
    
    analysis = Analysis(
        user_id=user_id,
        resume_id=resume_id,
        job_description=job_description,
        analysis_result=ai_result["full_analysis"],
        match_score=ai_result["match_score"]
    )
    
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    return analysis


from datetime import datetime
from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    id: int
    user_id: int
    resume_id: int
    job_description: str
    analysis_result: str
    match_score: int
    analyzed_at: datetime

    class Config:
        from_attributes = True
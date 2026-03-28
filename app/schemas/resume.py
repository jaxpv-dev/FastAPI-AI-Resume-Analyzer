from datetime import datetime
from pydantic import BaseModel

class ResumeResponse(BaseModel):
    id: int
    file_name: str
    user_id: int
    uploaded_at: datetime


    class Config:
        from_attributes = True
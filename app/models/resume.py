from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from datetime import datetime, timezone
from app.db.session import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable =False)
    file_name = Column(String(250), nullable=False)
    file_path = Column(String(500), nullable=False)
    extracted_text = Column(Text)
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


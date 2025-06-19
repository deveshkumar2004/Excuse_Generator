from pydantic import BaseModel
from datetime import datetime

class ExcuseRequest(BaseModel):
    scenario: str
    urgency: str = "moderate"
    language: str = "en"
    schedule_at: datetime | None = None 

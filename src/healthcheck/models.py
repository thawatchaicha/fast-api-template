from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.database import Base

class HealthCheck(Base):
    __tablename__ = "healthcheck"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

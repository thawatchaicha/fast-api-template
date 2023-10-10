from pydantic import BaseModel
from datetime import datetime

class HealthCheckBase(BaseModel):
    status: str

class HealthCheckCreate(HealthCheckBase):
    pass

class HealthCheck(HealthCheckBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

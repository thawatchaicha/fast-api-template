from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from src.database import get_db

router = APIRouter()

@router.get("/healthcheck", response_model=schemas.HealthCheck)
def get_health_status(db: Session = Depends(get_db)):
    db_healthcheck = crud.get_healthcheck(db)
    if db_healthcheck is None:
        raise HTTPException(status_code=404, detail="No healthcheck record found")
    return db_healthcheck

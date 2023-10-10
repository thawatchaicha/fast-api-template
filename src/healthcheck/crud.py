from sqlalchemy.orm import Session

from . import models, schemas

def get_healthcheck(db: Session):
    return db.query(models.HealthCheck).first()

def create_healthcheck_status(db: Session, healthcheck: schemas.HealthCheckCreate):
    db_healthcheck = models.HealthCheck(**healthcheck.dict())
    db.add(db_healthcheck)
    db.commit()
    db.refresh(db_healthcheck)
    return db_healthcheck

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import Depends
from .config import Settings

settings = Settings()

DATABASE_URL = settings.DATABASE_URL

# Recommended pool settings
engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # Default is 5, adjust as needed
    max_overflow=20,       # Extra connections beyond pool_size
    pool_timeout=30,       # Seconds to wait before giving up on a connection
    pool_recycle=1800,     # Recycle connections after 30 mins
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

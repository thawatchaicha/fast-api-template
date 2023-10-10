from fastapi import FastAPI
from src.database import Base, engine

from src.healthcheck.router import router as healthcheck_router
from src.users.router import router as users_router

from .config import Settings
from .database import get_db

# Dynamically load the .env file based on the ENV you want. For example, to load the local env:
Settings.model_config["env_file"] = "local.env"
settings = Settings()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(healthcheck_router, prefix="", tags=["healthcheck"])
app.include_router(users_router, prefix="/api", tags=["users"])

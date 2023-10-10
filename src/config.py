# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    ENVIRONMENT: str

    model_config = SettingsConfigDict(env_file=".env") # This will be overridden in main.py

from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "iitr")
    VERSION: str = os.getenv("VERSION", "1.0.0")
    DESCRIPTION: str = os.getenv("DESCRIPTION", "An application for filing Income Tax Returns")

    # Database Settings
    # DATABASE_URL: str = "postgresql://username:password@localhost/db_name"

    class Config:
        env_file = ".env"

settings = Settings()

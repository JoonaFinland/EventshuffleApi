from pydantic import AnyUrl
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "app_"

    DATABASE_URL: str
    ENVIRONMENT: str = "dev"
    ALLOWED_CORS_ORIGINS: set[AnyUrl]
    BASE_URL: str = ""
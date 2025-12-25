from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # MongoDB
    MONGODB_URL: str
    DATABASE_NAME: str = "ranoshisdas_db_user"

    # JWT Auth
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7 days

    # API Config
    API_V1_PREFIX: str = "/api"
    PROJECT_NAME: str = "Smart ToDo API"

    class Config:
        env_file = ".env"           # Load variables from .env
        case_sensitive = True       # Environment variables are case-sensitive

# Instantiate settings
settings = Settings()

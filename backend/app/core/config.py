from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List, Optional


class Settings(BaseSettings):
    PROJECT_NAME: str = "Restaurierungsentitaeten"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = "sqlite:///./restaurierungsentitaeten.db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # ML Settings
    GLINER_MODEL_NAME: str = "urchade/gliner_multi-v2.1"
    SPACY_MODEL: str = "de_dep_news_trf"
    DEFAULT_THRESHOLD: float = 0.5
    MAX_TEXT_LENGTH: int = 50000
    
    # Institution Auth (configure these for your institution)
    AUTH_SERVICE_URL: Optional[str] = None
    AUTH_CLIENT_ID: Optional[str] = None
    AUTH_CLIENT_SECRET: Optional[str] = None
    
    class Config:
        env_file = ".env"


settings = Settings()
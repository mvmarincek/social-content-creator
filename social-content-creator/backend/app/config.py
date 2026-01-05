from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    openai_api_key: str = ""
    anthropic_api_key: Optional[str] = None
    elevenlabs_api_key: Optional[str] = None
    fal_api_key: Optional[str] = None
    lumalabs_api_key: Optional[str] = None
    
    database_url: str = "sqlite:///./social_content.db"
    chroma_persist_directory: str = "./chroma_db"
    
    host: str = "0.0.0.0"
    port: int = 8000
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

os.environ["OPENAI_API_KEY"] = settings.openai_api_key
if settings.elevenlabs_api_key:
    os.environ["ELEVENLABS_API_KEY"] = settings.elevenlabs_api_key
if settings.fal_api_key:
    os.environ["FAL_KEY"] = settings.fal_api_key

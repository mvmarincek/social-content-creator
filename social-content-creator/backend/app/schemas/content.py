from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class Platform(str, Enum):
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"
    LINKEDIN = "linkedin"
    TWITTER = "twitter"

class ContentType(str, Enum):
    POST = "post"
    REELS = "reels"
    STORIES = "stories"
    CAROUSEL = "carousel"
    VIDEO = "video"
    SHORT = "short"

class ToneOfVoice(str, Enum):
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    MOTIVATIONAL = "motivational"
    EDUCATIONAL = "educational"
    HUMOROUS = "humorous"
    INSPIRATIONAL = "inspirational"

class ContentRequest(BaseModel):
    description: str = Field(..., description="Descrição do conteúdo desejado")
    platform: Platform = Field(default=Platform.INSTAGRAM)
    content_type: ContentType = Field(default=ContentType.POST)
    tone: ToneOfVoice = Field(default=ToneOfVoice.CASUAL)
    reference_profile: Optional[str] = Field(None, description="URL do perfil de referência")
    reference_text: Optional[str] = Field(None, description="Texto de referência para estilo")
    user_copy: Optional[str] = Field(None, description="Copy/texto fornecido pelo usuário")
    generate_image: bool = Field(default=False)
    generate_video: bool = Field(default=False)
    generate_audio: bool = Field(default=False)
    additional_instructions: Optional[str] = None

class AnalyzeProfileRequest(BaseModel):
    profile_url: str = Field(..., description="URL do perfil para analisar")
    platform: Platform = Field(default=Platform.INSTAGRAM)

class GenerateContentRequest(BaseModel):
    prompt: str = Field(..., description="Prompt para geração de conteúdo")
    session_id: Optional[str] = Field(None, description="ID da sessão para manter contexto")

class ContentResponse(BaseModel):
    success: bool
    content: str
    session_id: Optional[str] = None
    error: Optional[str] = None

class ProfileAnalysis(BaseModel):
    success: bool
    analysis: str
    error: Optional[str] = None

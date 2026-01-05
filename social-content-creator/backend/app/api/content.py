from fastapi import APIRouter, HTTPException
from app.schemas import (
    ContentRequest,
    AnalyzeProfileRequest,
    GenerateContentRequest,
    ContentResponse,
    ProfileAnalysis,
)
from app.teams.content_master import content_master_team
from app.agents.profile_analyzer import profile_analyzer_agent
import uuid

router = APIRouter(prefix="/api/content", tags=["content"])

@router.post("/create", response_model=ContentResponse)
async def create_content(request: ContentRequest):
    try:
        prompt = f"""
Crie conteúdo para {request.platform.value} do tipo {request.content_type.value}.

BRIEFING:
{request.description}

CONFIGURAÇÕES:
- Plataforma: {request.platform.value}
- Tipo: {request.content_type.value}
- Tom de voz: {request.tone.value}
- Gerar imagem com IA: {"Sim" if request.generate_image else "Não"}
- Gerar vídeo com IA: {"Sim" if request.generate_video else "Não"}
- Gerar áudio/narração: {"Sim" if request.generate_audio else "Não"}
"""
        if request.reference_profile:
            prompt += f"\nPERFIL DE REFERÊNCIA: {request.reference_profile}"
        
        if request.reference_text:
            prompt += f"\nTEXTO DE REFERÊNCIA PARA ESTILO:\n{request.reference_text}"
        
        if request.user_copy:
            prompt += f"\nCOPY/TEXTO FORNECIDO PELO USUÁRIO:\n{request.user_copy}"
        
        if request.additional_instructions:
            prompt += f"\nINSTRUÇÕES ADICIONAIS:\n{request.additional_instructions}"
        
        prompt += "\n\nCrie o conteúdo completo e pronto para publicação."
        
        response = await content_master_team.arun(prompt)
        
        return ContentResponse(
            success=True,
            content=response.content,
            session_id=str(uuid.uuid4())
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-profile", response_model=ProfileAnalysis)
async def analyze_profile(request: AnalyzeProfileRequest):
    try:
        prompt = f"""
Analise o perfil de {request.platform.value}: {request.profile_url}

Forneça:
1. Estilo e tom de voz predominante
2. Tipos de conteúdo mais postados
3. Hashtags mais utilizadas
4. Padrões de engajamento identificados
5. Elementos visuais característicos
6. Frequência e horários de postagem (se identificável)
7. Pontos fortes e diferenciais
8. Sugestões para replicar o estilo
"""
        response = await profile_analyzer_agent.arun(prompt)
        
        return ProfileAnalysis(
            success=True,
            analysis=response.content
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat", response_model=ContentResponse)
async def chat_with_agent(request: GenerateContentRequest):
    try:
        response = await content_master_team.arun(request.prompt)
        
        return ContentResponse(
            success=True,
            content=response.content,
            session_id=request.session_id or str(uuid.uuid4())
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Content Creator API"}

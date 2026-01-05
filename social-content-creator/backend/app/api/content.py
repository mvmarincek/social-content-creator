from fastapi import APIRouter, HTTPException, UploadFile, File
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
import openai
import tempfile
import os

router = APIRouter(prefix="/api/content", tags=["content"])

@router.post("/create", response_model=ContentResponse)
async def create_content(request: ContentRequest):
    try:
        base_prompt = f"""
Crie conteudo para {request.platform.value} do tipo {request.content_type.value}.

BRIEFING:
{request.description}

CONFIGURACOES:
- Plataforma: {request.platform.value}
- Tipo: {request.content_type.value}
- Tom de voz: {request.tone.value}

REGRA OBRIGATORIA: Voce DEVE criar EXATAMENTE 3 OPCOES DIFERENTES de conteudo.
Formate assim:
## Opcao 1: [Nome Criativo]
[conteudo completo]

## Opcao 2: [Nome Criativo]  
[conteudo completo]

## Opcao 3: [Nome Criativo]
[conteudo completo]

Cada opcao deve ter copy, hashtags e abordagem DIFERENTE das outras.
"""
        if request.generate_image:
            base_prompt += """
ACAO OBRIGATORIA - GERAR IMAGEM REAL:
O usuario quer uma IMAGEM REAL gerada por IA.
Voce DEVE delegar para o Image Creator que vai usar a ferramenta generate_media.
A resposta DEVE conter a URL real da imagem gerada (https://...png ou .jpg).
NAO descreva a imagem - GERE a imagem real usando a ferramenta FalTools.
"""
        if request.generate_video:
            base_prompt += """
ACAO OBRIGATORIA - GERAR VIDEO REAL:
O usuario quer um VIDEO REAL gerado por IA.
Voce DEVE delegar para o Video Creator que vai usar a ferramenta generate_media.
A resposta DEVE conter a URL real do video gerado (https://...mp4).
NAO descreva o video - GERE o video real usando a ferramenta FalTools.
"""
        if request.generate_audio:
            base_prompt += """
GERAR AUDIO/NARRACAO:
O usuario solicitou narracao/audio para o conteudo.
"""
        if request.reference_profile:
            base_prompt += f"\nPERFIL DE REFERENCIA: {request.reference_profile}"
        
        if request.reference_text:
            base_prompt += f"\nTEXTO DE REFERENCIA PARA ESTILO:\n{request.reference_text}"
        
        if request.user_copy:
            base_prompt += f"\nCOPY/TEXTO FORNECIDO PELO USUARIO:\n{request.user_copy}"
        
        if request.additional_instructions:
            base_prompt += f"\nINSTRUCOES ADICIONAIS:\n{request.additional_instructions}"
        
        base_prompt += "\n\nCrie as 3 opcoes de conteudo completas e prontas para publicacao. Se foi solicitado imagem ou video, inclua as URLs reais geradas."
        
        response = await content_master_team.arun(base_prompt)
        
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

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        suffix = os.path.splitext(file.filename)[1] if file.filename else ".mp3"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        try:
            client = openai.OpenAI()
            with open(tmp_path, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
            return {"success": True, "transcription": transcript}
        finally:
            os.unlink(tmp_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

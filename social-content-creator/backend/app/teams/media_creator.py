from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.image_creator import image_creator_agent
from app.agents.video_creator import video_creator_agent
from app.agents.audio_creator import audio_creator_agent

media_creator_team = Team(
    name="Media Creator",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        image_creator_agent,
        video_creator_agent,
        audio_creator_agent,
    ],
    instructions=[
        "Você é a equipe de criação de mídia visual e auditiva.",
        "Coordene os especialistas para criar os assets necessários.",
        "",
        "Fluxo de trabalho:",
        "1. Analise o tipo de conteúdo solicitado",
        "",
        "2. Para IMAGENS:",
        "   - Delegue ao Image Creator",
        "   - Especifique dimensões conforme plataforma",
        "   - Para carrossel, crie múltiplas imagens coesas",
        "",
        "3. Para VÍDEOS:",
        "   - Delegue ao Video Creator para conceito visual",
        "   - Delegue ao Audio Creator para narração/trilha",
        "   - Combine as diretrizes em um pacote de produção",
        "",
        "4. Se o usuário forneceu assets próprios:",
        "   - Use-os como base",
        "   - Crie apenas o que está faltando",
        "",
        "Mantenha consistência visual com a identidade da marca.",
    ],
    markdown=True,
    enable_agentic_context=True,
    share_member_interactions=True,
)

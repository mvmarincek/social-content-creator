from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.image_creator import image_creator_agent
from app.agents.video_creator import video_creator_agent
from app.agents.audio_creator import audio_creator_agent

media_creator_team = Team(
    name="Media Creator",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        image_creator_agent,
        video_creator_agent,
        audio_creator_agent,
    ],
    instructions=[
        "Você é a equipe de criação de mídia visual e auditiva.",
        "Para IMAGENS: crie prompts detalhados para DALL-E.",
        "Para VÍDEOS: crie conceito visual e direção de áudio.",
        "Mantenha consistência visual com a identidade da marca.",
    ],
    markdown=True,
)

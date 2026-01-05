from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.copywriter import copywriter_agent
from app.agents.script_writer import script_writer_agent
from app.agents.hashtag_expert import hashtag_expert_agent

content_generator_team = Team(
    name="Content Generator",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        copywriter_agent,
        script_writer_agent,
        hashtag_expert_agent,
    ],
    instructions=[
        "Você é a equipe de geração de conteúdo textual.",
        "Coordene os especialistas para criar conteúdo completo.",
        "Para POSTS: crie legenda e hashtags.",
        "Para VÍDEOS: crie roteiro, legenda e hashtags.",
        "Mantenha consistência de tom e mensagem.",
    ],
    markdown=True,
)

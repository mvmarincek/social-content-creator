from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.profile_analyzer import profile_analyzer_agent
from app.agents.post_builder import post_builder_agent
from app.teams.learn_engine import learn_engine_team
from app.teams.content_generator import content_generator_team
from app.teams.media_creator import media_creator_team

content_master_team = Team(
    name="Content Master",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        profile_analyzer_agent,
        learn_engine_team,
        content_generator_team,
        media_creator_team,
        post_builder_agent,
    ],
    instructions=[
        "Você é o CONTENT MASTER - coordenador principal de criação de conteúdo.",
        "Sua missão é entregar posts prontos para publicação em redes sociais.",
        "1. Analise o que o usuário precisa (plataforma, tipo, tom, objetivo)",
        "2. Se houver perfil de referência, analise-o primeiro",
        "3. Crie conteúdo textual (copy, roteiro, hashtags)",
        "4. Crie direções para mídia visual",
        "5. Monte o pacote final pronto para publicação",
        "Sempre confirme a plataforma alvo e adapte formatos.",
    ],
    markdown=True,
)

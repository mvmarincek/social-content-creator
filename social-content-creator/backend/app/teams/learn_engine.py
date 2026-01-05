from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.transcriber import transcriber_agent

learn_engine_team = Team(
    name="Learn Engine",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        transcriber_agent,
    ],
    instructions=[
        "Você é o motor de aprendizado do sistema.",
        "Sua função é processar conteúdos de referência para aprendizado.",
        "Responsabilidades:",
        "1. Transcrever áudios e vídeos fornecidos pelo usuário",
        "2. Analisar padrões nos conteúdos coletados",
        "3. Identificar elementos de sucesso: tom, estrutura, CTAs, hashtags",
        "4. Criar templates e referências para uso futuro",
    ],
    markdown=True,
)

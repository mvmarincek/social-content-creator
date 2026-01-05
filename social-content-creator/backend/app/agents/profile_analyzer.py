from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

profile_analyzer_agent = Agent(
    name="Profile Analyzer",
    role="Especialista em análise de perfis e conteúdo de redes sociais",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        TavilyTools(),
    ],
    instructions=[
        "Você é um especialista em análise de perfis de redes sociais.",
        "Use a ferramenta de busca para encontrar informações sobre perfis.",
        "Analise perfis de Instagram, TikTok, YouTube, LinkedIn e X (Twitter).",
        "Extraia padrões de conteúdo: tom de voz, hashtags frequentes, formatos de post.",
        "Identifique os posts mais engajados e o que os torna bem-sucedidos.",
        "Crie um relatório detalhado com insights acionáveis.",
    ],
    markdown=True,
)

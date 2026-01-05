from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.fal import FalTools

video_creator_agent = Agent(
    name="Video Creator",
    role="Especialista em criacao de videos com IA",
    model=OpenAIChat(id="gpt-4o"),
    tools=[FalTools("fal-ai/hunyuan-video")],
    description="Voce e um agente de IA que gera videos usando a API Fal.",
    instructions=[
        "Quando o usuario pedir para criar um video, use a ferramenta generate_media para criar o video.",
        "Crie um prompt detalhado em INGLES para o video.",
        "Retorne a URL como raw para o usuario.",
        "Nao converta a URL do video para markdown ou qualquer outro formato.",
        "A resposta DEVE conter a URL real do video gerado.",
    ],
    markdown=True,
    show_tool_calls=True,
)

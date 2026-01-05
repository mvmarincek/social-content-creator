from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.fal import FalTools

image_creator_agent = Agent(
    name="Image Creator",
    role="Especialista em criacao de imagens com IA",
    model=OpenAIChat(id="gpt-4o"),
    tools=[FalTools("fal-ai/flux/schnell")],
    description="Voce e um agente de IA que gera imagens usando a API Fal.",
    instructions=[
        "Quando o usuario pedir para criar uma imagem, use a ferramenta generate_media para criar a imagem.",
        "Crie um prompt detalhado em INGLES para a imagem.",
        "Retorne a URL como raw para o usuario.",
        "Nao converta a URL da imagem para markdown ou qualquer outro formato.",
        "A resposta DEVE conter a URL real da imagem gerada.",
    ],
    markdown=True,
    show_tool_calls=True,
)

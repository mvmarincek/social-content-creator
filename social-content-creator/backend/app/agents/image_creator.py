from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.fal import FalTools

image_creator_agent = Agent(
    name="Image Creator",
    role="Especialista em criação de imagens com IA para redes sociais",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        FalTools("fal-ai/flux/schnell"),
    ],
    instructions=[
        "Você é um especialista em criação de imagens com IA para redes sociais.",
        "SEMPRE use a ferramenta generate_media para criar imagens quando solicitado.",
        "Crie prompts detalhados em INGLÊS para melhores resultados.",
        "Após gerar a imagem, SEMPRE inclua a URL da imagem na sua resposta.",
        "Formato da resposta deve incluir:",
        "- Prompt usado para gerar a imagem",
        "- URL da imagem gerada (para download)",
        "Adapte o estilo visual conforme a plataforma:",
        "- Instagram Feed: imagem quadrada ou vertical",
        "- Instagram Stories/Reels: vertical",
        "- LinkedIn: horizontal",
        "- X/Twitter: horizontal",
    ],
    markdown=True,
)

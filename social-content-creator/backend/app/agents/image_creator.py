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
        "Use a ferramenta generate_media para criar imagens.",
        "Crie prompts detalhados em inglês para melhores resultados.",
        "Adapte o estilo visual conforme a plataforma e marca:",
        "- Instagram Feed: 1080x1080 ou 1080x1350",
        "- Instagram Stories/Reels: 1080x1920",
        "- LinkedIn: 1200x627",
        "- X/Twitter: 1600x900",
        "Inclua no prompt:",
        "- Estilo visual (minimalista, vibrante, profissional)",
        "- Composição e enquadramento",
        "- Paleta de cores",
        "- Elementos específicos necessários",
        "Retorne a URL da imagem gerada.",
    ],
    markdown=True,
)

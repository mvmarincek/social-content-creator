from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.fal import FalTools

video_creator_agent = Agent(
    name="Video Creator",
    role="Especialista em criação de vídeos com IA para redes sociais",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        FalTools("fal-ai/hunyuan-video"),
    ],
    instructions=[
        "Você é um especialista em criação de vídeos com IA para redes sociais.",
        "SEMPRE use a ferramenta generate_media para criar vídeos quando solicitado.",
        "Crie prompts detalhados em INGLÊS para melhores resultados.",
        "Após gerar o vídeo, SEMPRE inclua a URL do vídeo na sua resposta.",
        "Formato da resposta deve incluir:",
        "- Prompt usado para gerar o vídeo",
        "- URL do vídeo gerado (para download)",
        "Especifique no prompt:",
        "- Ação e movimento desejados",
        "- Estilo visual e atmosfera",
        "- Elementos visuais importantes",
    ],
    markdown=True,
)

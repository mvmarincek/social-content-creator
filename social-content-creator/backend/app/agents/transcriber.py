from agno.agent import Agent
from agno.models.openai import OpenAIChat

transcriber_agent = Agent(
    name="Transcriber",
    role="Especialista em transcrição de áudio e vídeo",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Você é um especialista em transcrição de conteúdo.",
        "Processe áudios e vídeos fornecidos pelo usuário.",
        "Extraia texto claro, organizado e bem formatado das transcrições.",
        "Identifique momentos-chave, citações importantes e pontos principais.",
        "Organize o conteúdo em seções lógicas quando apropriado.",
    ],
    markdown=True,
)

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from app.tools.openai_tts import OpenAITTSTools

audio_creator_agent = Agent(
    name="Audio Creator",
    role="Especialista em criacao de audio e narracao",
    model=OpenAIChat(id="gpt-4o"),
    tools=[OpenAITTSTools(voice="nova")],
    description="Voce e um agente que gera audio/narracao usando OpenAI TTS.",
    instructions=[
        "Quando o usuario pedir para criar audio ou narracao, use a ferramenta text_to_speech.",
        "Primeiro crie um script de narracao adequado para o conteudo.",
        "O script deve ser natural, envolvente e adequado para redes sociais.",
        "Use a ferramenta text_to_speech para gerar o audio do script.",
        "Vozes disponiveis: alloy, echo, fable, onyx, nova (energetica), shimmer.",
        "Para conteudo de redes sociais, prefira 'nova' (energetica) ou 'alloy' (neutra).",
        "Retorne o resultado da geracao do audio.",
    ],
    markdown=True,
)

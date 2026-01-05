from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.fal import FalTools

video_creator_agent = Agent(
    name="Video Creator",
    role="Especialista em criacao de videos com IA",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        FalTools("fal-ai/hunyuan-video"),
    ],
    instructions=[
        "Voce e um especialista em criacao de videos com IA.",
        "REGRA OBRIGATORIA: Voce DEVE SEMPRE usar a ferramenta generate_media para criar o video.",
        "NUNCA apenas descreva o video - voce DEVE gerar o video real usando a ferramenta.",
        "Passos obrigatorios:",
        "1. Crie um prompt detalhado em INGLES descrevendo o video",
        "2. Use a ferramenta generate_media com esse prompt",
        "3. Aguarde a geracao e obtenha a URL do video",
        "4. Retorne a URL do video gerado para download",
        "Sua resposta DEVE conter a URL real do video (ex: https://...mp4)",
        "Se a ferramenta falhar, informe o erro - mas SEMPRE tente usar a ferramenta primeiro.",
    ],
    markdown=True,
)

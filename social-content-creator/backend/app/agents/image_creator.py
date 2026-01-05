from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.fal import FalTools

image_creator_agent = Agent(
    name="Image Creator",
    role="Especialista em criacao de imagens com IA",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        FalTools("fal-ai/flux/schnell"),
    ],
    instructions=[
        "Voce e um especialista em criacao de imagens com IA.",
        "REGRA OBRIGATORIA: Voce DEVE SEMPRE usar a ferramenta generate_media para criar a imagem.",
        "NUNCA apenas descreva a imagem - voce DEVE gerar a imagem real usando a ferramenta.",
        "Passos obrigatorios:",
        "1. Crie um prompt detalhado em INGLES descrevendo a imagem",
        "2. Use a ferramenta generate_media com esse prompt",
        "3. Aguarde a geracao e obtenha a URL da imagem",
        "4. Retorne a URL da imagem gerada para download",
        "Sua resposta DEVE conter a URL real da imagem (ex: https://...png ou https://...jpg)",
        "Se a ferramenta falhar, informe o erro - mas SEMPRE tente usar a ferramenta primeiro.",
    ],
    markdown=True,
)

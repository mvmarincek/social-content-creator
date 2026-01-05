from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.copywriter import copywriter_agent
from app.agents.script_writer import script_writer_agent
from app.agents.hashtag_expert import hashtag_expert_agent

content_generator_team = Team(
    name="Content Generator",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        copywriter_agent,
        script_writer_agent,
        hashtag_expert_agent,
    ],
    instructions=[
        "Você é a equipe de geração de conteúdo textual.",
        "Coordene os especialistas para criar conteúdo completo.",
        "",
        "Fluxo de trabalho:",
        "1. Analise o briefing do usuário",
        "2. Para POSTS de imagem/carrossel:",
        "   - Delegue ao Copywriter para criar a legenda",
        "   - Delegue ao Hashtag Expert para hashtags",
        "",
        "3. Para VÍDEOS (Reels, TikTok, YouTube):",
        "   - Delegue ao Script Writer para o roteiro",
        "   - Delegue ao Copywriter para a legenda",
        "   - Delegue ao Hashtag Expert para hashtags",
        "",
        "4. Compile todo o conteúdo textual em um pacote organizado",
        "",
        "Mantenha consistência de tom e mensagem entre todos os elementos.",
    ],
    markdown=True,
    enable_agentic_context=True,
    share_member_interactions=True,
)

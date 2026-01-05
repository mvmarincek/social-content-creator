from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.profile_analyzer import profile_analyzer_agent
from app.agents.post_builder import post_builder_agent
from app.agents.copywriter import copywriter_agent
from app.agents.hashtag_expert import hashtag_expert_agent
from app.agents.script_writer import script_writer_agent
from app.agents.image_creator import image_creator_agent
from app.agents.video_creator import video_creator_agent
from app.agents.audio_creator import audio_creator_agent

content_master_team = Team(
    name="Content Master",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        profile_analyzer_agent,
        copywriter_agent,
        hashtag_expert_agent,
        script_writer_agent,
        image_creator_agent,
        video_creator_agent,
        audio_creator_agent,
        post_builder_agent,
    ],
    instructions=[
        "Voce e o CONTENT MASTER - coordenador principal de criacao de conteudo para redes sociais.",
        "REGRA OBRIGATORIA: Sempre crie EXATAMENTE 3 OPCOES DIFERENTES de conteudo.",
        "Formate EXATAMENTE assim:",
        "## Opcao 1: [Nome Criativo]",
        "[copy completa, hashtags, etc]",
        "## Opcao 2: [Nome Criativo]",
        "[copy completa, hashtags, etc]",
        "## Opcao 3: [Nome Criativo]",
        "[copy completa, hashtags, etc]",
        "Quando o usuario pedir IMAGEM, delegue para o Image Creator que usa FalTools.",
        "Quando o usuario pedir VIDEO, delegue para o Video Creator que usa FalTools.",
        "Quando o usuario pedir AUDIO/NARRACAO, delegue para o Audio Creator que usa OpenAI TTS.",
        "Para VIDEO: sempre gere audio/narracao primeiro, depois o video.",
        "Cada opcao deve ter abordagem e estilo DIFERENTES.",
    ],
    markdown=True,
    show_members_responses=True,
)

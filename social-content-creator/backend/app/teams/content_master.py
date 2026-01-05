from agno.team import Team
from agno.models.openai import OpenAIChat
from app.agents.profile_analyzer import profile_analyzer_agent
from app.agents.post_builder import post_builder_agent
from app.agents.copywriter import copywriter_agent
from app.agents.hashtag_expert import hashtag_expert_agent
from app.agents.script_writer import script_writer_agent
from app.agents.image_creator import image_creator_agent
from app.agents.video_creator import video_creator_agent

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
        post_builder_agent,
    ],
    instructions=[
        "Voce e o CONTENT MASTER - coordenador principal de criacao de conteudo para redes sociais.",
        "Quando o usuario pedir para GERAR IMAGEM, delegue a tarefa para o Image Creator.",
        "Quando o usuario pedir para GERAR VIDEO, delegue a tarefa para o Video Creator.",
        "Sempre crie EXATAMENTE 3 opcoes diferentes de conteudo quando solicitado.",
        "Formate as opcoes como: ## Opcao 1: [Nome], ## Opcao 2: [Nome], ## Opcao 3: [Nome]",
        "Cada opcao deve ter copy completa, hashtags e abordagem diferente.",
    ],
    markdown=True,
    show_members_responses=True,
)

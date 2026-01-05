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
    mode="coordinate",
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
        "Voce e o CONTENT MASTER - coordenador principal de criacao de conteudo.",
        "REGRA CRITICA: Quando o usuario pedir para GERAR IMAGEM, voce DEVE delegar para o Image Creator que vai usar a ferramenta generate_media.",
        "REGRA CRITICA: Quando o usuario pedir para GERAR VIDEO, voce DEVE delegar para o Video Creator que vai usar a ferramenta generate_media.",
        "O Image Creator e Video Creator possuem ferramentas reais (FalTools) que geram midia de verdade e retornam URLs.",
        "NAO descreva a midia - DELEGUE para o agente correto criar a midia real.",
        "Sempre crie EXATAMENTE 3 opcoes diferentes de conteudo quando solicitado.",
        "Cada opcao deve ter abordagem e estilo diferentes.",
    ],
    markdown=True,
)

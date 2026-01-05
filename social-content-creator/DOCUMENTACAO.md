# Social Content Creator - Documentacao Completa

## Visao Geral

Sistema de criacao de conteudo para redes sociais usando IA multiagente com o framework Agno. O sistema analisa perfis, gera copys, cria imagens e videos automaticamente.

**URLs de Producao:**
- Frontend: https://social-content-creator.vercel.app/
- Backend: https://social-content-creator-zvue.onrender.com
- Repositorio: https://github.com/mvmarincek/social-content-creator

---

## Arquitetura do Sistema

```
social-content-creator/
├── backend/                    # API FastAPI + Agno
│   ├── app/
│   │   ├── agents/            # 9 agentes especializados
│   │   ├── api/               # Endpoints REST
│   │   ├── schemas/           # Modelos Pydantic
│   │   ├── teams/             # Equipes de agentes
│   │   └── config.py          # Configuracoes
│   ├── main.py                # Entry point
│   └── requirements.txt       # Dependencias Python
├── frontend/                   # React + Vite + TypeScript
│   ├── src/
│   │   ├── components/        # Componentes React
│   │   ├── lib/               # API client e tipos
│   │   └── App.tsx            # Componente principal
│   └── package.json           # Dependencias Node
└── DOCUMENTACAO.md            # Este arquivo
```

---

## Stack Tecnologico

### Backend
- **Python 3.11+**
- **FastAPI** - Framework web async
- **Agno** - Framework de agentes IA (https://docs.agno.com)
- **OpenAI GPT-4o** - Modelo de linguagem
- **OpenAI Whisper** - Transcricao de audio
- **FalTools** - Geracao de imagens e videos
- **TavilyTools** - Busca na web

### Frontend
- **React 18** + **Vite**
- **TypeScript**
- **Tailwind CSS**
- **Lucide React** - Icones
- **React Markdown** - Renderizacao de markdown

### Deploy
- **Render** - Backend (auto-deploy do GitHub)
- **Vercel** - Frontend (auto-deploy do GitHub)

---

## Agentes do Sistema

### 1. Profile Analyzer (`profile_analyzer.py`)
- Analisa perfis de redes sociais
- Identifica tom de voz, hashtags, padroes
- Usa TavilyTools para buscar informacoes

### 2. Copywriter (`copywriter.py`)
- Cria textos persuasivos
- Adapta tom conforme plataforma
- Headlines, CTAs, legendas

### 3. Hashtag Expert (`hashtag_expert.py`)
- Pesquisa hashtags relevantes
- Analisa tendencias
- Sugere combinacoes estrategicas

### 4. Script Writer (`script_writer.py`)
- Cria roteiros para videos
- Estrutura gancho, desenvolvimento, CTA
- Adapta duracao por plataforma

### 5. Image Creator (`image_creator.py`)
- Gera imagens com IA usando FalTools
- Modelo: `fal-ai/flux/schnell`
- Cria prompts detalhados em ingles
- **SEMPRE retorna URL da imagem gerada**

### 6. Video Creator (`video_creator.py`)
- Gera videos com IA usando FalTools
- Modelo: `fal-ai/hunyuan-video`
- **SEMPRE retorna URL do video gerado**

### 7. Audio Creator (`audio_creator.py`)
- Cria narracoes (placeholder para ElevenLabs)

### 8. Post Builder (`post_builder.py`)
- Monta o post final completo
- Combina todos os elementos

### 9. Transcriber (`transcriber.py`)
- Transcreve audios e videos
- Extrai pontos principais

---

## Equipes (Teams)

### Content Master Team (`content_master.py`)
- Equipe principal que coordena todos os agentes
- Modo: `coordinate` (orquestra os agentes)
- Responsavel por gerar as 3 opcoes de conteudo

### Media Creator Team (`media_creator.py`)
- Especializada em criacao de midia
- Agrupa image_creator e video_creator

### Learn Engine Team (`learn_engine.py`)
- Aprende estilos de perfis
- Armazena padroes identificados

---

## Endpoints da API

### `POST /api/content/create`
Cria conteudo com 3 opcoes diferentes.

**Request:**
```json
{
  "description": "Criar post sobre produtividade",
  "platform": "instagram",
  "content_type": "post",
  "tone": "motivational",
  "reference_profile": "https://instagram.com/exemplo",
  "reference_text": "Texto de referencia...",
  "user_copy": "Meu texto base...",
  "generate_image": true,
  "generate_video": false,
  "generate_audio": false,
  "additional_instructions": "Foco em empreendedores"
}
```

**Response:**
```json
{
  "success": true,
  "content": "## Opcao 1: [Nome]\n...\n## Opcao 2: [Nome]\n...\n## Opcao 3: [Nome]\n...",
  "session_id": "uuid"
}
```

### `POST /api/content/transcribe`
Transcreve arquivo de audio usando OpenAI Whisper.

**Request:** `multipart/form-data` com campo `file`

**Response:**
```json
{
  "success": true,
  "transcription": "Texto transcrito do audio..."
}
```

### `POST /api/content/analyze-profile`
Analisa perfil de rede social.

**Request:**
```json
{
  "profile_url": "https://instagram.com/exemplo",
  "platform": "instagram"
}
```

### `POST /api/content/chat`
Chat livre com o agente.

**Request:**
```json
{
  "prompt": "Sua mensagem",
  "session_id": "opcional"
}
```

### `GET /api/content/health`
Health check do servico.

---

## Variaveis de Ambiente

### Backend (Render)
```
OPENAI_API_KEY=sk-...        # Obrigatoria - GPT-4o e Whisper
TAVILY_API_KEY=tvly-...      # Obrigatoria - Busca web
FAL_KEY=...                   # Obrigatoria - Geracao de imagens/videos
```

### Frontend (Vercel)
```
VITE_API_URL=https://social-content-creator-zvue.onrender.com
```

---

## Fluxo de Funcionamento

### 1. Usuario Cria Conteudo
```
1. Usuario preenche formulario (descricao, plataforma, tom, etc.)
2. Se anexou audio:
   a. Frontend envia audio para /transcribe
   b. Backend usa Whisper para transcrever
   c. Transcricao e adicionada ao prompt
3. Frontend envia request para /create
4. Backend monta prompt com instrucoes para 3 opcoes
5. Content Master Team coordena agentes
6. Se generate_image=true:
   a. Image Creator gera imagem com FalTools
   b. URL da imagem e incluida na resposta
7. Se generate_video=true:
   a. Video Creator gera video com FalTools
   b. URL do video e incluida na resposta
8. Backend retorna as 3 opcoes em markdown
9. Frontend parseia e exibe em 3 cards
10. Usuario pode copiar ou baixar midia
```

### 2. Transcricao de Audio
```
1. Usuario anexa arquivo de audio
2. Audio e destacado em roxo na interface
3. Ao clicar "Criar Conteudo":
   a. Mensagem "Transcrevendo audio..."
   b. Audio enviado para /transcribe
   c. Whisper processa e retorna texto
4. Transcricao e usada como base do conteudo
```

---

## Componentes do Frontend

### ContentCreator.tsx
Componente principal com:
- Formulario de criacao
- Upload de arquivos (imagem, audio, video)
- Exibicao de 3 cards com opcoes
- Deteccao automatica de URLs de midia
- Botoes de copiar e baixar

**Estados principais:**
- `description`, `platform`, `contentType`, `tone` - Configuracoes
- `uploadedFiles` - Arquivos anexados
- `result` - Resposta do backend
- `contentOptions` - Array com 3 opcoes parseadas
- `selectedOption` - Opcao selecionada pelo usuario
- `loadingMessage` - Mensagem de progresso

**Funcoes importantes:**
- `handleCreate()` - Processa transcricao e cria conteudo
- `parseContentOptions()` - Extrai 3 opcoes do markdown
- `extractUrls()` - Encontra URLs de midia no texto
- `transcribeAudio()` - Chama API de transcricao

### ProfileAnalyzer.tsx
Analise de perfis de referencia.

### Chat.tsx
Interface de chat com o agente.

---

## Como Rodar Localmente

### Backend
```bash
cd social-content-creator/backend

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Configurar .env
echo "OPENAI_API_KEY=sk-..." > .env
echo "TAVILY_API_KEY=tvly-..." >> .env
echo "FAL_KEY=..." >> .env

# Rodar
python main.py
# ou
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd social-content-creator/frontend

# Instalar dependencias
npm install

# Configurar .env
echo "VITE_API_URL=http://localhost:8000" > .env

# Rodar
npm run dev
```

---

## Deploy

### Render (Backend)
1. Conectar repo GitHub
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Adicionar variaveis de ambiente
5. Deploy automatico a cada push

### Vercel (Frontend)
1. Conectar repo GitHub
2. Root Directory: `social-content-creator/frontend`
3. Build Command: `npm run build`
4. Output Directory: `dist`
5. Adicionar VITE_API_URL nas variaveis
6. Deploy automatico a cada push

---

## APIs Externas

### OpenAI
- **GPT-4o**: Modelo de linguagem para todos os agentes
- **Whisper**: Transcricao de audio
- Pricing: https://openai.com/pricing

### Tavily
- Busca web para pesquisar perfis e tendencias
- https://tavily.com
- Plano gratuito: 1000 requests/mes

### Fal.ai
- Geracao de imagens: `fal-ai/flux/schnell`
- Geracao de videos: `fal-ai/hunyuan-video`
- https://fal.ai
- Precisa de creditos

---

## Troubleshooting

### "Erro ao conectar com o servidor"
- Verificar se backend esta rodando
- Verificar VITE_API_URL no frontend
- Verificar CORS no backend

### Imagem/Video nao gerado
- Verificar FAL_KEY esta configurada
- Verificar creditos no fal.ai
- Logs do Render para erros

### Transcricao falhou
- Verificar OPENAI_API_KEY
- Formato de audio suportado (mp3, wav, m4a, etc.)
- Tamanho maximo: 25MB

### 3 opcoes nao aparecem separadas
- Backend pode estar retornando formato diferente
- Verificar se resposta contem "## Opcao 1:", "## Opcao 2:", etc.

---

## Proximas Melhorias Sugeridas

1. **Historico de conteudos** - Salvar geracoes anteriores
2. **Edicao inline** - Editar opcoes antes de copiar
3. **Agendamento** - Integrar com APIs das redes sociais
4. **Templates** - Salvar configuracoes favoritas
5. **ElevenLabs** - Integracao para narracao de audio
6. **Preview de midia** - Mostrar imagem/video inline no card

---

## Contato

Repositorio: https://github.com/mvmarincek/social-content-creator

---

*Documentacao atualizada em: Janeiro 2026*

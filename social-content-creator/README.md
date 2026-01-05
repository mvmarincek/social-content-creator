# Social Content Creator

Plataforma de criacao de conteudo para redes sociais com sistema multiagente usando Agno Framework.

## Arquitetura

```
                    CONTENT MASTER (Team Principal)
                              |
        +----------+----------+----------+----------+
        |          |          |          |          |
   Profile     Learn      Content     Media      Post
   Analyzer    Engine     Generator   Creator    Builder
    Agent       Team        Team       Team       Agent
                  |           |          |
             Transcriber  Copywriter  Image Creator
                          Script      Video Creator
                          Writer      Audio Creator
                          Hashtag
                          Expert
```

## Requisitos

- Python 3.10+
- Node.js 18+
- Chave de API da OpenAI

## Instalacao

### 1. Backend

```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar Variaveis de Ambiente

```bash
# Copiar arquivo de exemplo
copy .env.example .env

# Editar .env com suas chaves de API
# Obrigatorio: OPENAI_API_KEY
```

### 3. Frontend

```bash
cd frontend
npm install
```

## Executando

### Terminal 1 - Backend

```bash
cd backend
venv\Scripts\activate
python main.py
```

O backend estara disponivel em: http://localhost:8000
Documentacao da API: http://localhost:8000/docs

### Terminal 2 - Frontend

```bash
cd frontend
npm run dev
```

O frontend estara disponivel em: http://localhost:5173

## Uso

### 1. Criar Conteudo (Formulario)

- Selecione a plataforma (Instagram, TikTok, etc)
- Escolha o tipo de conteudo (Post, Reels, etc)
- Defina o tom de voz
- Descreva o que voce precisa
- Clique em "Criar Conteudo"

### 2. Chat (Conversacao Livre)

- Converse diretamente com o Content Master
- Descreva livremente o que precisa
- O agente coordenara os especialistas

### 3. Analisar Perfil

- Cole a URL de um perfil de referencia
- O sistema analisara padroes e estilos
- Use os insights para suas criacoes

## Estrutura do Projeto

```
social-content-creator/
├── backend/
│   ├── app/
│   │   ├── agents/          # Agentes individuais
│   │   ├── teams/           # Times de agentes
│   │   ├── api/             # Endpoints da API
│   │   ├── schemas/         # Modelos Pydantic
│   │   └── config.py        # Configuracoes
│   ├── main.py              # Entry point
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    ├── src/
    │   ├── components/      # Componentes React
    │   ├── lib/             # API client e tipos
    │   └── App.tsx          # Componente principal
    ├── package.json
    └── vite.config.ts
```

## Agentes e Tools

| Agente | Funcao | Tools Agno |
|--------|--------|------------|
| Profile Analyzer | Analisa perfis de redes sociais | WebsiteTools, YouTubeTools, DuckDuckGoTools |
| Transcriber | Transcreve audios e videos | MLXTranscribeTools |
| Copywriter | Cria textos persuasivos | GPT-4o |
| Script Writer | Cria roteiros de videos | GPT-4o |
| Hashtag Expert | Pesquisa hashtags | DuckDuckGoTools |
| Image Creator | Gera imagens com IA | DalleTools |
| Video Creator | Cria conceitos de video | GPT-4o |
| Audio Creator | Direciona narracao | GPT-4o |
| Post Builder | Monta post final | GPT-4o |

## APIs Opcionais

Para recursos avancados, configure estas APIs:

- **ElevenLabs**: Geracao de voz realista
- **Fal AI**: Geracao de imagens e videos
- **Luma Labs**: Videos cinematograficos

---

## Deploy Gratuito Online

### Opcao 1: Railway (Backend) + Vercel (Frontend)

#### Backend no Railway

1. Crie conta em https://railway.app (gratis com GitHub)

2. Clique em "New Project" > "Deploy from GitHub repo"

3. Selecione o repositorio e configure:
   - Root Directory: `backend`
   
4. Adicione as variaveis de ambiente:
   ```
   OPENAI_API_KEY=sk-sua-chave
   FRONTEND_URL=https://seu-frontend.vercel.app
   ```

5. Railway vai detectar o Python e fazer deploy automatico

6. Copie a URL gerada (ex: `https://seu-app.railway.app`)

#### Frontend na Vercel

1. Crie conta em https://vercel.com (gratis com GitHub)

2. Clique em "New Project" > importe o repositorio

3. Configure:
   - Framework Preset: Vite
   - Root Directory: `frontend`

4. Adicione variavel de ambiente:
   ```
   VITE_API_URL=https://seu-app.railway.app
   ```

5. Clique em "Deploy"

---

### Opcao 2: Render (Backend) + Vercel (Frontend)

#### Backend no Render

1. Crie conta em https://render.com (gratis)

2. New > Web Service > Connect GitHub repo

3. Configure:
   - Name: social-content-creator-api
   - Root Directory: backend
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. Adicione Environment Variables:
   ```
   OPENAI_API_KEY=sk-sua-chave
   FRONTEND_URL=https://seu-frontend.vercel.app
   ```

5. Copie a URL (ex: `https://social-content-creator-api.onrender.com`)

#### Frontend na Vercel (mesmo processo acima)

---

### Opcao 3: Koyeb (Backend Gratuito)

1. Crie conta em https://koyeb.com

2. Create App > GitHub > Selecione repo

3. Configure:
   - Builder: Dockerfile
   - Working Directory: backend
   
4. Environment Variables:
   ```
   OPENAI_API_KEY=sk-sua-chave
   PORT=8000
   ```

---

### Subir para GitHub (necessario para deploy)

```bash
cd c:\Teste_verdent\social-content-creator

# Inicializar repositorio
git init
git add .
git commit -m "Initial commit: Social Content Creator"

# Criar repo no GitHub e conectar
git remote add origin https://github.com/seu-usuario/social-content-creator.git
git branch -M main
git push -u origin main
```

---

### Limites dos Planos Gratuitos

| Servico | Limite Gratuito |
|---------|-----------------|
| Railway | $5/mes de credito, hiberna apos inatividade |
| Render | 750h/mes, hiberna apos 15min inativo |
| Vercel | Ilimitado para projetos pessoais |
| Koyeb | 1 app, 512MB RAM |

**Dica**: Render e Railway hibernam o backend quando inativo. A primeira requisicao apos hibernacao demora ~30s para "acordar".

## Licenca

MIT

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import content_router
from app.config import settings

app = FastAPI(
    title="Social Content Creator",
    description="Plataforma de criação de conteúdo para redes sociais com IA multiagente",
    version="1.0.0",
)

allowed_origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    os.getenv("FRONTEND_URL", ""),
]
allowed_origins = [o for o in allowed_origins if o]
allowed_origins.append("*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(content_router)

@app.get("/")
async def root():
    return {
        "name": "Social Content Creator API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/content/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )

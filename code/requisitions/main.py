from fastapi import FastAPI
from modules.router import router
from modules.cobertura import router as cobertura_router
from modules.qwen import router as qwen_router

app = FastAPI(title='Projeto - Infraestrutura Digital no Brasil')

app.include_router(router)
app.include_router(cobertura_router)
app.include_router(qwen_router)
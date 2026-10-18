from fastapi import FastAPI
from modules.router import router

app = FastAPI(title='Capitais e suas respectivas Coberturas 4g')

app.include_router(router)
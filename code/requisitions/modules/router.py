from pathlib import Path
from fastapi import APIRouter, HTTPException
import pandas as pd

router = APIRouter()

lista_capitais = [
    {"capital": "São Paulo", "cobertura": 98.5},
    {"capital": "Manaus", "cobertura": 76.2},
    {"capital": "Porto Alegre", "cobertura": 95.3},
    {"capital": "Teresina", "cobertura": 88.1},
    {"capital": "Rio Branco", "cobertura": 61.4},
]

@router.get('/capitais')
async def listar_capital():
    return {"lista de capitais": lista_capitais}


@router.post('/capitais')
async def add_capital(capital: str, cobertura: float):
    nova_capital = {'capital': capital, 'cobertura': cobertura}
    lista_capitais.append(nova_capital)
    return {
        'mensagem': f'{capital} adicionada na lista com sucesso!',
        'lista_atualizada': lista_capitais,
        
        }
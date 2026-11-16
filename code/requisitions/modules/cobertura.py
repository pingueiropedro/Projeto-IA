from pathlib import Path

import pandas as pd
from fastapi import APIRouter, HTTPException

router = APIRouter()

DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "raw"
CSV = DATA_DIR / "cobertura_estados_4g_anatel_mar2026.csv"


@router.get("/cobertura")
def listar_cobertura():
    try:
        dados = pd.read_csv(CSV)
        return dados.to_dict(orient="records")
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Arquivo de cobertura não encontrado"
        ) 
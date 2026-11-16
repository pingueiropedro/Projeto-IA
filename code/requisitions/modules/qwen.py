from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline

router = APIRouter()

modelo = None


class TextoEntrada(BaseModel):
    texto: str = Field(min_length=15, max_length=1500)


class TextoSaida(BaseModel):
    texto_original: str
    tipo_analise: str
    resultado: str



@router.post("/processar_texto", response_model=TextoSaida)
def processar_texto(dados: TextoEntrada):
    global modelo

    if modelo is None:
        try:
            modelo = pipeline(
                "text-generation",
                model="Qwen/Qwen2.5-0.5B-Instruct",
                device=-1
            )

        except Exception as erro:
            print(f"Erro ao carregar Qwen: {erro}")
            raise HTTPException(
                status_code=503,
                detail="Modelo Qwen indisponível."
            )

    mensagens = [
        {
            "role": "user",
            "content": dados.texto
        }
    ]

    try:
        resposta = modelo(
            mensagens,
            max_new_tokens=100,
            do_sample=False
        )
        resultado = resposta[0]["generated_text"][-1]["content"]
        

    except Exception as erro:
        print(f"Erro ao gerar resposta: {erro}")

        raise HTTPException(
            status_code=500,
            detail="Erro ao processar o texto com Qwen."
        )


    return TextoSaida(
        texto_original=dados.texto,
        tipo_analise="resumo",
        resultado=resultado
    )

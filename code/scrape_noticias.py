import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

raiz_projeto = Path(__file__).resolve().parent.parent
DATA_DIR = raiz_projeto / 'data' / 'raw'
DATA_DIR.mkdir(parents=True, exist_ok=True)


urls = [
    'https://teletime.com.br/11/08/2026/tim-roaming-agenda/',
    'https://teletime.com.br/18/09/2026/anatel-nega-recurso-oi-escolas/',
    'https://teletime.com.br/16/09/2026/teles-conseguem-cautelar-que-pode-mudar-resultado-do-leilao-de-700-mhz/',
    'https://teletime.com.br/18/09/2026/anatel-mvnos-da-telecall/'
]

titulos = []
corpos = []

for indice, link in enumerate(urls, start=1):

    url = requests.get(link)
    url_sopa = BeautifulSoup(url.text, 'html.parser')

    titulo = url_sopa.find('h1').get_text(strip=True)
    paragrafos = url_sopa.select('p')
    corpo = [p.get_text(strip=True) for p in paragrafos if len(p.get_text(strip=True)) > 40]

    titulos.append(titulo)
    corpos.append(' '.join(corpo))

    print(f'Título: {titulo}')
    print(f'Parágrafos extraídos: {len(corpo)}')


df = pd.DataFrame({
    'titulo': titulos,
    'corpo': corpos,
    'link': urls
})


caminho_csv = DATA_DIR / 'noticias_anatel.csv'
df.to_csv(caminho_csv, index=False, encoding='utf-8')

corpus = ' '.join(titulos) + ' ' + ' '.join(corpos)
caminho_txt = DATA_DIR / 'corpus_noticias.txt'
caminho_txt.write_text(corpus, encoding='utf-8')
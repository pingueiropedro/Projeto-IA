import re
import time
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

TAG = 'https://teletime.com.br/tag/anatel/'
FEED = 'https://teletime.com.br/tag/anatel/feed/'
SAIDA = Path(__file__).resolve().parent.parent.parent / 'data' / 'raw' / 'noticias_anatel.csv'
HEADERS = {'User-Agent': 'Mozilla/5.0 (projeto academico)'}
PADRAO = r'https://teletime\.com\.br/\d{2}/\d{2}/\d{4}/'   # matéria = data na URL

# as 4 matérias que você já tinha (garantia)
links = [
    'https://teletime.com.br/11/08/2026/tim-roaming-agenda/',
    'https://teletime.com.br/18/09/2026/anatel-nega-recurso-oi-escolas/',
    'https://teletime.com.br/16/09/2026/teles-conseguem-cautelar-que-pode-mudar-resultado-do-leilao-de-700-mhz/',
    'https://teletime.com.br/18/09/2026/anatel-mvnos-da-telecall/',
]

# 1a. links pelo feed RSS
try:
    texto = requests.get(FEED, headers=HEADERS, timeout=15).text
    achados = re.findall(r'<link>\s*(https?://[^<\s]+)\s*</link>', texto)
    print(f'Feed: {len(achados)} links')
    for l in achados:
        if re.match(PADRAO, l) and l not in links:
            links.append(l)
except Exception as erro:
    print(f'Feed falhou: {erro}')

# 1b. links pela página da tag (páginas 1 a 3)
for pagina in range(1, 4):
    url = TAG if pagina == 1 else f'{TAG}page/{pagina}/'
    try:
        sopa = BeautifulSoup(requests.get(url, headers=HEADERS, timeout=15).text, 'html.parser')
    except Exception as erro:
        print(f'Página {pagina} falhou: {erro}')
        continue
    antes = len(links)
    for a in sopa.select('a[href]'):
        href = urljoin(url, a['href']).split('#')[0].split('?')[0]
        if re.match(PADRAO, href) and href not in links:
            links.append(href)
    print(f'Página {pagina}: {len(links) - antes} links novos')
    time.sleep(1)

links = links[:10]
print(f'{len(links)} links para baixar')

# 2. título e texto de cada matéria
linhas = []
for link in links:
    try:
        sopa = BeautifulSoup(requests.get(link, headers=HEADERS, timeout=15).text, 'html.parser')
        paragrafos = [p.get_text(strip=True) for p in sopa.select('p')]
        linhas.append({
            'titulo': sopa.find('h1').get_text(strip=True),
            'corpo': ' '.join(p for p in paragrafos if len(p) > 40),
            'link': link,
        })
        print('OK  ', link)
    except Exception as erro:
        print('ERRO', link, erro)
    time.sleep(1)

# 3. salvar
pd.DataFrame(linhas).to_csv(SAIDA, index=False)
print(f'{len(linhas)} notícias salvas em {SAIDA}')
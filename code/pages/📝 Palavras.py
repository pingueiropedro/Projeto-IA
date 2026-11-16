import re
from collections import Counter
from pathlib import Path

import pandas as pd
import streamlit as st
from wordcloud import WordCloud

DATA_DIR = Path(__file__).parent.parent.parent / 'data' / 'raw'

STOPWORDS = set('''a o as os um uma uns umas de do da dos das em no na nos nas por para com sem sob sobre
entre até após ante e ou mas que se como quando onde porque pois já não mais menos muito muita muitos
também só ao aos à às pelo pela pelos pelas este esta estes estas esse essa esses essas isso isto aquele
aquela ele ela eles elas seu sua seus suas dele dela deles delas foi ser são era será serão tem têm ter
teve há havia está estão estava sido ainda sobre cada outro outra outros outras mesmo mesma num numa
nesta neste nessa nesse disso desta deste dessa desse segundo disse afirmou ano anos'''.split())

st.header('Palavras mais frequentes nas notícias')


@st.cache_data(ttl=3600)
def carregar_texto():
  csv = DATA_DIR / 'noticias_anatel.csv'
  if csv.exists():
    df = pd.read_csv(csv)
    return ' '.join(df['titulo'].fillna('')) + ' ' + ' '.join(df['corpo'].fillna(''))
  txt = DATA_DIR / 'corpus_noticias.txt'
  return txt.read_text(encoding='utf-8') if txt.exists() else ''


@st.cache_data(ttl=3600)
def contar(texto, tamanho_minimo):
  palavras = re.findall(r'[a-záàâãéêíóôõúç0-9]+', texto.lower())
  return Counter(p for p in palavras
                 if len(p) >= tamanho_minimo and p not in STOPWORDS)


texto = carregar_texto()
if not texto:
  st.warning('Sem notícias em data/raw/. Rode: python code/src/scrape_noticias.py')
  st.stop()

col1, col2 = st.columns(2)
top_n = col1.slider('Quantidade de palavras', 10, 100, 50, key='top_n')
tamanho_min = col2.slider('Tamanho mínimo da palavra', 3, 8, 4, key='tamanho_min')

frequencias = contar(texto, tamanho_min)
nuvem = WordCloud(width=900, height=450, background_color='white') \
    .generate_from_frequencies(dict(frequencias.most_common(top_n)))
st.image(nuvem.to_array(), use_container_width=True)

st.subheader('Top 15 palavras')
top = pd.DataFrame(frequencias.most_common(15), columns=['palavra', 'ocorrências'])
st.bar_chart(top.set_index('palavra'))
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).parent.parent.parent / 'data' / 'raw'

st.header('Notícias sobre Anatel')
st.caption('Coletadas do Teletime com Beautiful Soup (code/src/scrape_noticias.py)')


@st.cache_data(ttl=3600)
def carregar_noticias():
  caminho = DATA_DIR / 'noticias_anatel.csv'
  if caminho.exists():
    return pd.read_csv(caminho)
  return pd.DataFrame(columns=['titulo', 'data', 'corpo', 'link'])


df = carregar_noticias()
st.metric('Notícias coletadas', len(df))

busca = st.text_input('Buscar no título ou no texto')
if busca:
  mascara = (df['titulo'].str.contains(busca, case=False, na=False)
             | df['corpo'].str.contains(busca, case=False, na=False))
  df = df[mascara]

colunas = [c for c in ['data', 'titulo', 'link'] if c in df.columns]
st.dataframe(df[colunas], use_container_width=True)
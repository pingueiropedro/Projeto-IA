from pathlib import Path
import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).parent.parent.parent / 'data' / 'raw'

st.header('Titulo das Noticias sobre Anatel')
st.caption('Titulos extraidos com a utilidade do BeautifulSoup')


@st.cache_data
def carregar_noticias():
  caminho = DATA_DIR / 'noticias_anatel.csv'
  if caminho.exists():
    return pd.read_csv(caminho)
  return pd.DataFrame(columns=['titulo', 'link'])


df_noticias = carregar_noticias()

st.metric('Noticias coletadas', len(df_noticias))
st.dataframe(df_noticias[['titulo', 'link']], use_container_width=True)

st.header('Envie seus próprios dados')
st.markdown(
    'Envie um CSV complementar (ex: dados municipais) para incluir na análise'
)

if 'df_upload' not in st.session_state:
  st.session_state['df_upload'] = None

arquivo_enviado = st.file_uploader('Envie seu arquivo', type=['csv'])

if arquivo_enviado is not None:
  st.session_state['df_upload'] = pd.read_csv(arquivo_enviado)
  st.success(
      f'Arquivo recebido com {len(st.session_state["df_upload"])} linhas!'
  )
  st.balloons()

if st.session_state['df_upload'] is not None:
  st.subheader('Dados enviados pelo Usuário')
  st.dataframe(st.session_state['df_upload'], use_container_width=True)

  st.download_button(
      'Baixe os dados enviados (CSV)',
      data=st.session_state['df_upload'].to_csv(index=False).encode('utf-8'),
      file_name='dados_enviados.csv',
      mime='text/csv',
  )

  if st.button('Remover dados enviados'):
    st.session_state['df_upload'] = None
    st.rerun()
import requests
import streamlit as st 
import pandas as pd 

url = requests.get(r'http://127.0.0.1:8000/capitais')

st.title('Gestão de Capitais (FastAPI)')

# 1. POST - Formulário para enviar
with st.form('novo_cadastro'):
  capital = st.text_input('Capital:')
  cobertura = st.number_input('Cobertura (%):', value=80.0)

  if st.form_submit_button('Enviar'):
    res = requests.post(
        url, params={'capital': capital, 'cobertura': cobertura}
    )
    if res.status_code == 200:
      st.success('Enviado com sucesso!')
      st.rerun()

st.divider()

# 2. GET - Tabela para mostrar os dados da API
try:
  res_get = requests.get(url)
  dados = res_get.json()
  lista = dados.get('lista de capitais', dados)

  st.dataframe(pd.DataFrame(lista), use_container_width=True)

except:
  st.warning('Ligue a API no terminal com uvicorn!')
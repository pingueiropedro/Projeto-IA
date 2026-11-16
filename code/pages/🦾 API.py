import pandas as pd
import requests
import streamlit as st

API_URL = 'http://127.0.0.1:8000/capitais'
TIMEOUT = 5

st.title('Gestão de Capitais (FastAPI)')


with st.form('novo_cadastro'):
  capital = st.text_input('Capital:')
  cobertura = st.number_input('Cobertura (%):', min_value=0.0, max_value=100.0, value=80.0)
  enviado = st.form_submit_button('Enviar')

if enviado:
  
  if not capital.strip():
    st.warning('Informe o nome da capital.')
  
  else:
    try:
      res = requests.post(
          API_URL,
          params={'capital': capital.strip(), 'cobertura': cobertura},
          timeout=TIMEOUT,
      )
      
      res.raise_for_status()
      st.success(res.json().get('mensagem', 'Enviado com sucesso!'))
    
    except requests.exceptions.ConnectionError:
      st.error(f'Não consegui conectar em {API_URL}. Suba a API: '
               '`cd code/requisitions && uvicorn main:app --reload`')
    
    except requests.exceptions.RequestException as erro:
      st.error(f'Erro ao enviar para a API: {erro}')

st.divider()


try:
  res_get = requests.get(API_URL, timeout=TIMEOUT)
  res_get.raise_for_status()
  dados = res_get.json()
  lista = dados.get('lista de capitais', dados)
  
  st.dataframe(pd.DataFrame(lista), use_container_width=True)

except requests.exceptions.ConnectionError:
  st.warning(f'API fora do ar ({API_URL}). Rode: '
             '`cd code/requisitions && uvicorn main:app --reload`')

except requests.exceptions.RequestException as erro:
  st.error(f'Erro na requisição GET: {erro}')

except ValueError as erro:  
  st.error(f'A API respondeu algo que não é JSON: {erro}')
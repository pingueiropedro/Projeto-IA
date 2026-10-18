import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium

st.header('Amostra de dados')
st.markdown('**OBS:** Estrutura Provisoria apenas para a amostra de dados')


@st.cache_data
def carregar_amostra():
  return pd.DataFrame({
      'capital': [
          'São Paulo',
          'Manaus',
          'Teresina',
          'Rio Branco',
          'Porto Alegre',
      ],
      'regiao': ['Sudeste', 'Norte', 'Nordeste', 'Norte', 'Sul'],
      'cobertura': [98.5, 76.2, 88.1, 61.4, 95.3],
      'banda_larga_fixa': [4_500_000, 210_000, 680_000, 45_000, 800_500],
      'lat': [-23.549, -3.107, -5.089, -9.974, -30.028],
      'lon': [-46.639, -60.026, -42.802, -67.808, -51.229]
  })


amostra_dados = carregar_amostra()

if 'capitais_selecionadas' not in st.session_state:
  st.session_state['capitais_selecionadas'] = list(
      amostra_dados['capital'].unique()
  )

st.markdown('**Gráfico Interativo**')
regioes_selecionadas = st.multiselect(
    'Filtrar por Capital',
    options=amostra_dados['capital'].unique(),
    default=st.session_state['capitais_selecionadas'],
    key='capitais_selecionadas',
)

dados_filtrados = amostra_dados[
    amostra_dados['capital'].isin(st.session_state['capitais_selecionadas'])
]
st.dataframe(dados_filtrados, use_container_width=True)

st.divider()
st.subheader('🗺️ Mapeamento Geográfico de Cobertura')


if not dados_filtrados.empty:

    m = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

    # 2. Adiciona marcadores com popup/tooltip
    for idx, row in dados_filtrados.iterrows():
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"<b>{row['capital']}</b><br>Cobertura: {row['cobertura']}%",
            tooltip=row['capital']
        ).add_to(m)

    # 3. Renderiza o mapa com st_folium
    st_folium(m, width=700, height=450, use_container_width=True)
else:
    st.warning('Selecione ao menos uma capital no filtro para visualizar no mapa.')
    
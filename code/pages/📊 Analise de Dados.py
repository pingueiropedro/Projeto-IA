import folium
import pandas as pd
import requests
import streamlit as st
from streamlit_folium import st_folium

API_URL = "http://127.0.0.1:8000/cobertura"

st.header("📊 Cobertura 4G por estado")


@st.cache_data(ttl=60)
def carregar_dados():
    resposta = requests.get(API_URL, timeout=10)
    resposta.raise_for_status()
    return pd.DataFrame(resposta.json())


try:
    dados = carregar_dados()
except requests.RequestException as erro:
    st.error(f"Erro ao conectar com a API: {erro}")
    st.stop()


estados = st.multiselect(
    "Escolha os estados",
    options=dados["estado"].tolist(),
    default=dados["estado"].tolist()
)

filtrados = dados[dados["estado"].isin(estados)]

st.metric("Estados selecionados", len(filtrados))
st.dataframe(filtrados, use_container_width=True)

if not filtrados.empty:
    st.subheader("Cobertura 4G (%)")
    st.bar_chart(filtrados.set_index("uf")["cobertura"])

    st.subheader("🗺️ Mapa de cobertura")

    coordenadas = {
        "AC": [-9.97, -67.81], "AL": [-9.67, -35.74],
        "AP": [0.03, -51.07], "AM": [-3.12, -60.02],
        "BA": [-12.97, -38.50], "CE": [-3.73, -38.53],
        "DF": [-15.79, -47.88], "ES": [-20.32, -40.34],
        "GO": [-16.68, -49.25], "MA": [-2.53, -44.30],
        "MT": [-15.60, -56.10], "MS": [-20.47, -54.62],
        "MG": [-19.92, -43.94], "PA": [-1.46, -48.49],
        "PB": [-7.12, -34.86], "PR": [-25.43, -49.27],
        "PE": [-8.05, -34.88], "PI": [-5.09, -42.80],
        "RJ": [-22.91, -43.17], "RN": [-5.79, -35.21],
        "RS": [-30.03, -51.23], "RO": [-8.76, -63.90],
        "RR": [2.82, -60.67], "SC": [-27.59, -48.55],
        "SP": [-23.55, -46.63], "SE": [-10.91, -37.07],
        "TO": [-10.18, -48.33]
    }

    mapa = folium.Map(
        location=[-14.23, -51.92],
        zoom_start=4
    )

    for _, linha in filtrados.iterrows():
        local = coordenadas.get(linha["uf"])

        if local:
            folium.Marker(
                location=local,
                tooltip=linha["estado"],
                popup=f"{linha['estado']}: {linha['cobertura']}%"
            ).add_to(mapa)

    st_folium(mapa, height=450, width=700)

else:
    st.warning("Selecione pelo menos um estado.")

st.caption(
    "Dados de cobertura 4G por estado, março de 2026. "
    "Os marcadores indicam as capitais estaduais, "
    "mas os percentuais representam as UFs."
)

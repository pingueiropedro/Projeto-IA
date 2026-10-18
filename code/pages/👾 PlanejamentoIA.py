import streamlit as st

st.header("🤖 Planejamento de Integração com IA (LLMs)")
st.caption("Visão futura para aplicação de Modelos de Linguagem no projeto ODS 9")

st.markdown("""
Nesta etapa de preparação, foram mapeadas quatro frentes principais de aplicação de **Large Language Models (LLMs)** utilizando os dados coletados de notícias e cobertura de telecomunicações:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Resumo de Notícias")
    st.write("Geração de resumos executivos curtos das notícias raspadas do portal da Anatel para otimizar a leitura do usuário.")
    
    st.subheader("2. Classificação de Sentimento")
    st.write("Análise do tom dos comunicados regulatórios (Positivo, Neutro, Negativo) quanto aos avanços do ODS 9.")

with col2:
    st.subheader("3. Sistema de Q&A (Perguntas e Respostas)")
    st.write("Assistente virtual para responder dúvidas sobre a infraestrutura de telecomunicações com base no histórico de notícias.")
    
    st.subheader("4. Geração de Relatórios")
    st.write("Criação automática de diagnósticos textuais sobre as disparidades de cobertura entre as capitais brasileiras.")


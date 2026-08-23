import streamlit as st
import pandas as pd

st.title('Inclusão das Redes Móveis')
st.caption('Projeto Academico - ODS 9: Industria, Inovação e Infraaestrutura')

st.header('Sobre o projeto')
st.markdown('''A expansão de infraestrutura de telecomunicações no Brasil não é uniforme: 
as principais capitais e regiões metropolitanas concentram melhor cobertura de rede móvel e banda larga fixa, 
enquanto municipios do interior, especialmente em regiões do Norte e do Nordeste seguem com infraestrutura limitadas, ou praticamente inexistentes. 
Essa desigualdade de infraestruturaa é a base estrutural de outros problemas, como ate mesmo a exclusão digital de familias e pequenas empresas. 
A Anatel disponibiliza esses dados abertamente no próprio site deles, mas de uma forma técnica, muito das vezes de uma forma onde pessoas comuns não possam visualizar e entender.''')

st.header('Objetivo do Projeto')
st.markdown('Analisar como a falta de acesso a redes moveis e banda larga ocorrem, e quais regiões/municipios são mais afetados pela falta' \
'alem de entender como se pode facilitar o acesso a estas zonas carentes.')

st.header('Links uteis para informação')
c1, c2 = st.columns(2)

with c1:
    st.markdown('**Fonte de dados**')

    st.markdown('[Meu Município — Anatel/dados.gov.br]'
    '(https://dados.gov.br/dados/conjuntos-dados/meu-municipio---acessos-e-cobertura-de-telecomunicacoes)")')
    st.markdown("- [Painel de Cobertura Móvel (Anatel)](https://www.gov.br/anatel/pt-br/dados/infraestrutura/antenas-nos-municipios/paineis-de-dados)")
    st.markdown("- [Painel de Banda Larga Fixa (Anatel)](https://www.anatel.gov.br/paineis/acessos/banda-larga-fixa)")
with c2: 
    st.markdown('**Inspirações para o Projeto**')
    st.markdown("- [Conecta Brasil](https://conectabrasil.org/home)")
    st.markdown("- [Observatório do Terceiro Setor]"
    "(https://observatorio3setor.org.br/carrossel/lista-conheca-projetos-sociais-de-15-causas-diferentes/)")

st.header('Amostra de dados')
st.markdown('**OBS:** Estrutura Provisoria apenas para a amostra de dados')

amostra_dados = pd.DataFrame({
    'municipio': ['São Paulo', 'Manaus', 'Teresina', 'Rio Branco', 'Porto Alegre'],
    "regiao": ["Sudeste", "Norte", "Nordeste", "Norte", "Sul"],
    "cobertura": [98.5, 76.2, 88.1, 61.4, 95.3],
    "banda_larga_fixa": [4_500_000, 210_000, 680_000, 45_000, 800_500]
    })


st.bar_chart(data=amostra_dados,
             x='municipio',
             y='cobertura',
            x_label='Municipios',
              y_label='Cobertura 4G (%)',
              horizontal=False,
              use_container_width=True)

st.markdown('OBS: Foi utilizado um ambiente virtual (.venv) para a criação deste esboço')
st.divider()
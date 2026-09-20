import streamlit as st
import pandas as pd
from pathlib import Path
from collections import Counter
import re


st.title('Inclusão das Redes Móveis')
st.caption('Projeto Academico - ODS 9: Industria, Inovação e Infraaestrutura')

st.header('Sobre o projeto')
st.markdown('''A expansão de infraestrutura de telecomunicações no Brasil não é uniforme: 
as principais capitais e regiões metropolitanas concentram melhor cobertura de rede móvel e banda larga fixa, 
enquanto municipios do interior, especialmente em regiões do Norte e do Nordeste seguem com infraestrutura limitadas, ou praticamente inexistentes. 
Essa desigualdade de infraestruturaa é a base estrutural de outros problemas, como ate mesmo a exclusão digital de familias e pequenas empresas. 
A Anatel disponibiliza esses dados abertamente no próprio site deles, mas de uma forma técnica, muito das vezes de uma forma onde pessoas comuns não possam visualizar e entender.''')

st.header('Objetivo do Projeto')
st.markdown('Analisar como a falta de acesso a redes moveis e banda larga ocorrem, e quais regiões/municipios são mais afetados pela falta ' \
'além de entender como se pode facilitar o acesso a estas zonas carentes.')

st.header('Links uteis para informação')
c1, c2 = st.columns(2)

with c1:
    st.markdown('**Fonte de dados**')

    st.markdown('[Meu Município — Anatel/dados.gov.br]'
    '(https://dados.gov.br/dados/conjuntos-dados/meu-municipio---acessos-e-cobertura-de-telecomunicacoes)')
    st.markdown("- [Painel de Cobertura Móvel (Anatel)](https://www.gov.br/anatel/pt-br/dados/infraestrutura/antenas-nos-municipios/paineis-de-dados)")
    st.markdown("- [Painel de Banda Larga Fixa (Anatel)](https://www.anatel.gov.br/paineis/acessos/banda-larga-fixa)")
with c2: 
    st.markdown('**Inspirações para o Projeto**')
    st.markdown("- [Conecta Brasil](https://conectabrasil.org/home)")
    st.markdown("- [Observatório do Terceiro Setor]"
    "(https://observatorio3setor.org.br/carrossel/lista-conheca-projetos-sociais-de-15-causas-diferentes/)")

st.header('Amostra de dados')
st.markdown('**OBS:** Estrutura Provisoria apenas para a amostra de dados')

@st.cache_data
def carregar_amostra():
    return pd.DataFrame({
        'capital': ['São Paulo', 'Manaus', 'Teresina', 'Rio Branco', 'Porto Alegre'],
        "regiao": ["Sudeste", "Norte", "Nordeste", "Norte", "Sul"],
        "cobertura": [98.5, 76.2, 88.1, 61.4, 95.3],
        "banda_larga_fixa": [4_500_000, 210_000, 680_000, 45_000, 800_500]
        })

amostra_dados = carregar_amostra()

st.markdown('**Gráfico Interativo**')
regioes_selecionadas = st.multiselect(
    'Filtrar por Capital',
    options=amostra_dados['capital'].unique(),
    default=amostra_dados['capital'].unique(),
    key='filtar_capital'
)

dados_filtrados = amostra_dados[amostra_dados['capital'].isin(regioes_selecionadas)]
st.dataframe(dados_filtrados,
             use_container_width=True)
st.bar_chart(data=dados_filtrados,
             x='capital',
             y='cobertura',
            x_label='Municipios',
              y_label='Cobertura 4G (%)',
              horizontal=False,
              use_container_width=True)


st.markdown('OBS: Foi utilizado um ambiente virtual (.venv) para a criação deste esboço')

st.divider()

DATA_DIR = Path(__file__).parent.parent / 'data' / 'raw'

st.header('Titulo das Noticias sobre Anatel')
st.caption('Titulos extraidos com a utilidade do BeautifulSoup')
@st.cache_data
def carregar_noticias():
    return pd.read_csv(DATA_DIR / 'noticias_anatel.csv')

df_noticias = carregar_noticias()

st.metric('Noticias coletadas', len(df_noticias))
st.dataframe(df_noticias[['titulo', 'link']], use_container_width=True)

st.header('Envie seus próprios dados')
st.markdown('Envie um CSV complementar (ex: dados municipais) para incluir na análise')

arquivo_enviado = st.file_uploader('Envie seu arquivo', type=['csv'])

if arquivo_enviado is not None:
    df_upload = pd.read_csv(arquivo_enviado)
    sucesso = st.success(f'Arquivo recebido com {len(df_upload)} linhas!')
    if sucesso:
        st.balloons()
    st.dataframe(df_upload, use_container_width=True)

st.download_button(
    'Baixe os dados filtrados (CSV)',
    data=dados_filtrados.to_csv(index=False).encode('utf-8'),
    file_name='dados_filtrados.csv',
    mime='text/csv'

)

st.subheader('Palavras mais frequentes')

@st.cache_data
def carregar_corpus():
    return (DATA_DIR / 'corpus_noticias.txt').read_text(encoding='utf-8')

corpus = carregar_corpus()

palavras_vazias = {
    'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'para', 'com', 'um', 'uma',
    'os', 'as', 'no', 'na', 'por', 'se', 'ao', 'dos', 'das', 'é', 'não',
    'anatel', 'sobre', 'foi', 'ser', 'mais', 'como', 'entre', 'já'
}

palavras = re.findall(r'\b[a-zà-ú]+\b', corpus.lower())
palavras_filtradas = [p for p in palavras if p not in palavras_vazias and len(p) > 3]

contagem = Counter(palavras_filtradas).most_common(15)

df_palavras = pd.DataFrame(contagem, columns=['palavra', 'frequencia'])
st.bar_chart(df_palavras.set_index('palavra'))

st.divider()
st.caption('Fonte: Painéis de Dados Abertos da Anatel · Notícias extraídas com Beautiful Soup')
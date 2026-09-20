# Painel de Infraestrutura Digital no Brasil
 | ODS 9 - Indústria, Inovação e Infraestrutura
 TP2

## Escopo do Projeto 

O projeto consiste no desenvolvimento de um dashboard, que consolida e visualiza indicadores de infraestrutura de telecomunicações no Brasil - cobertura de rede móvel (Como exemplo o 3G/4G e até mesmo o mais recente modelo 5G) e disponibilidade de banda larga fixa com base em dados abertos da Anatel. A aplicação permitirá comparar a infraestrutura dísponivel entre regiões e municípios.

## Problema de negócio

A expansão de infraestrutura de telecomunicações no Brasil não é uniforme: as principais capitais e regiões metropolitanas concentram melhor cobertura de rede móvel e banda larga fixa, enquanto municipios do interior, especialmente em regiões do Norte e do Nordeste seguem com infraestrutura limitadas, ou praticamente inexistentes. 

Essa desigualdade de infraestruturaa é a base estrutural de outros problemas, como ate mesmo a exclusão digital de familias e pequenas empresas. 

A Anatel disponibiliza esses dados abertamente no próprio site deles, mas de uma forma técnica, muito das vezes de uma forma onde pessoas comuns não possam visualizar e entender.


## Objetivos do Projeto

1 - Consolidar indicadores de cobertura de rede móvel (3G/4G) e banda larga fixa por municipio/região

2 - Construir visualizações de dados que evidenciam municipios/regiões com infraestrutura mais limitada

3 - Tornar tal conhecimento desses indicadores a uma acessibilidade a publico não-técnico

## Metas e indicadores de sucesso 


### Meta
Consolidar dados de infraestrutura de rede movel por municipio 
### Indicador de sucesso
Pipeline de dados reprodutível, cobrindo cobertura móvel e banda larga fixa

### Meta
Visualizar disparidades regionais
### Indicador de sucesso
Gráficos comparando pelo menos 3 regiões/UFs

### Meta
Validar a utilidade do painel
### Indicador de sucesso
Feedback de pelo menos 1 usuario do publico-alvo


## ODS atendido

O ODS escolhido foi o de item 9(Industria, Inovação e Infraestruturaa) e se trata de uma expansão de infraestrtura e promção de inovação, incluindo o acesso universal e preços acessíveis a internet como meta explicita.

A infraestrutura de telecomunicações, a cobertura móvel e banda larga fixa, é a base física que viabiliza qualquer avanço em inclusão digital, inovação e desenvolvimento ecônomico local/regional. Ao mapear por regiões onde são atingidas por esta falta de técnologia, o projeto contribui para uma tomada de decisões para futuras melhorias sobre o tópico.

## Público Alvo

- Empresas de telecomunicação e investidores, avaliando expansão de redes em regiões com carência;

- Pesquisadores e estudantes de infraestrutura, tecnologia, desenvolvimento regional e até mesmo da própria area de dados; 

- Formuladores de Politicas Publicas; 

- Profissionais da área de Negócios, com foco em telecomunicação

## Arquitetura Técnica (TP2)

- **Interface**: Streamlit, com filtros interativos (multiselect) ligados a session_state do estado escolhido

- **Extração de dados**: Scraping com BeautifulSoup extraido de sites da Anatel, gravados separadamente do app.py em 'data/raw/' (CSV e TXT)

- **Performance com cache**: cache (@sr.cache_data) com aplicação as funções de carregamento, evitando a releitura de cada função 
OBS: O cache armazena por apenas 1h 

- **Entrada/Download de dados do usuario**: upload de CSV complementar via st.file_upload(), para visualização dos mesmos em um DataFrame, e a função st.file_download() para fazer o download do mesmo 

- **Versionamento**: Github, com historico de commits por funcionalidade do projeto, indicando a evolução por meio da quantidade de commits


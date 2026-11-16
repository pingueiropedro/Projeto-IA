Painel de Infraestrutura Digital no Brasil

ODS 9 — Indústria, Inovação e Infraestrutura | TP2 e integração com LLM

1. Escopo do Projeto

Desenvolvimento de um dashboard interativo para análise da infraestrutura de telecomunicações no Brasil, com indicadores de cobertura 4G das 27 unidades federativas, visualizações geográficas, coleta de notícias e integração com inteligência artificial local.

2. Problema de Negócio

As desigualdades regionais de conectividade e a complexidade dos dados de telecomunicações dificultam a interpretação das informações. O projeto busca torná-las mais acessíveis por meio de visualizações e processamento de textos com IA.

3. Objetivos

Analisar e comparar indicadores de cobertura 4G.

Disponibilizar gráficos, tabelas e mapas interativos.

Integrar Streamlit e FastAPI.

Coletar notícias sobre telecomunicações por web scraping.

Processar textos utilizando um LLM local.

4. Metas e Indicadores

O projeto tem como metas consolidar os dados de cobertura 4G das 27 unidades federativas, disponibilizar gráficos e mapas interativos, integrar os serviços Streamlit e FastAPI e coletar notícias sobre telecomunicações em arquivos CSV e TXT.

Além disso, contempla a integração do modelo Qwen2.5-0.5B-Instruct para processamento de textos, com geração de respostas estruturadas e execução offline validada.
O projeto atende ao ODS 9, contribuindo para estudos sobre infraestrutura, inovação e conectividade.

Destina-se a estudantes, empresas de telecomunicações, gestores públicos e demais interessados.

6. Arquitetura Técnica

Streamlit, Pandas e Folium: dashboard, análise e mapas.

FastAPI: endpoints para capitais, cobertura estadual e processamento de textos.

BeautifulSoup e Requests: web scraping de notícias.
    Obs: Não houve necessidade no uso do Selenium para este projeto.

Transformers: execução local do Qwen2.5-0.5B-Instruct em CPU.

Pydantic: validação e respostas JSON.

HTTPException: tratamento de erros HTTP 500 e 503, com validação automática 422.

GitHub: versionamento do projeto.

7. Integração com Inteligência Artificial

Foi implementado o modelo Qwen2.5-0.5B-Instruct, disponibilizado pelo Hugging Face, integrado à rota POST /processar_texto.

A API recebe textos, gera respostas estruturadas e executa o modelo localmente, com funcionamento offline testado.

Como evolução, estão previstas funcionalidades de resumo de notícias, análise de sentimento, perguntas e respostas com RAG e geração automática de relatórios.
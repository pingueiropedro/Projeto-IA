Data Summary Report — Painel de Infraestrutura Digital no Brasil

ODS 9 | TP4 e Integração com LLM Local

1. Fontes de Dados

O projeto utiliza dados de cobertura móvel 4G das 27 unidades federativas, organizados em arquivos CSV, além de informações sobre capitais brasileiras e notícias de telecomunicações coletadas por web scraping.

As principais bases são cobertura_estados_4g_anatel_mar2026.csv, noticias_anatel.csv.

2. Preparação e Processamento

Os dados são carregados e organizados com Pandas para visualização em gráficos, tabelas e mapas interativos no Streamlit, utilizando Folium para representação geográfica.

As informações também são disponibilizadas por endpoints FastAPI, permitindo consultas estruturadas.

3. Coleta de Notícias

A coleta utiliza Requests e BeautifulSoup para extrair conteúdos relacionados à Anatel e ao setor de telecomunicações.

Os resultados são armazenados em CSV, permitindo consultas e futuras análises com inteligência artificial.

4. Processamento com LLM

Foi integrado o modelo Qwen2.5-0.5B-Instruct, utilizando Transformers e PyTorch para geração local de textos.

A rota POST /processar_texto recebe entradas de 15 a 1.500 caracteres, realiza o processamento e retorna um JSON com texto original, tipo de análise e resultado.

A execução offline foi testada com sucesso, sem necessidade de APIs externas para inferência.

5. Validação dos Dados e Respostas

O Pydantic valida as entradas e a estrutura das respostas da API. O FastAPI utiliza códigos HTTP 422, 500 e 503 para identificar entradas inválidas e falhas de processamento ou carregamento do modelo.

A validação dos valores de cobertura com a fonte oficial da Anatel permanece como uma etapa de conferência dos dados.

6. Resultado

O projeto reúne indicadores de infraestrutura digital, visualizações interativas, coleta de notícias e processamento local de linguagem natural, formando uma base para futuras aplicações de IA em telecomunicações.
# Painel de Infraestrutura Digital no Brasil — Data Summary Report

## Status atual (TP2)

O painel opera, nesta etapa, com uma **base de dados de exemplo** (5 capitais — uma por região do país), usada para validar a arquitetura da aplicação: filtros, cache, extração web e upload/download. A integração com a base oficial e completa da Anatel é o próximo passo do projeto, e as fontes abaixo documentam tanto o que já está em uso quanto o que está planejado.

## 1. Dados de cobertura — amostra (em uso)

Fonte: dados de exemplo, criados manualmente para desenvolvimento

Tipo de dado: Tabular, gerado em código (`pd.DataFrame`)

Granularidade: Por capital (1 por região — São Paulo, Manaus, Teresina, Rio Branco, Porto Alegre)

Variáveis: cobertura de rede móvel (%), acessos de banda larga fixa

Objetivo de uso: validar a interface (filtros, gráficos) antes da integração com a base oficial completa

Limitação conhecida: 5 registros não representam a distribuição real de infraestrutura entre os 5.000+ municípios brasileiros; serve apenas como prova de conceito

## 2. Notícias sobre Anatel — Teletime (em uso)

Fonte: portal Teletime (teletime.com.br), tag "Anatel"

Tipo de dado: Não estruturada, extraída via scraping (Beautiful Soup)

Coleta: script `scrape_noticias.py`, executado separadamente da aplicação, gravando em `data/raw/noticias_anatel.csv` e `data/raw/corpus_noticias.txt`

Volume coletado: 4 notícias (título, corpo do texto e link)

Objetivo de uso: contextualizar os dados quantitativos com notícias recentes sobre regulação e infraestrutura de telecomunicações; base para a análise de frequência de palavras exibida no painel

Tratamento: filtragem de parágrafos curtos (menos de 40 caracteres, tipicamente menu/rodapé do site); remoção de palavras vazias (stopwords) na contagem de frequência

## 3. CSV complementar do usuário (funcionalidade disponível)

Fonte: qualquer CSV enviado pelo usuário via upload no painel

Tipo de dado: Tabular, estrutura livre (definida pelo usuário)

Objetivo de uso: permitir que o público-alvo (ex: pesquisadores, formuladores de políticas) complemente a análise com dados próprios

Limitação conhecida: não há validação de schema; o app apenas exibe o que foi enviado, sem cruzar automaticamente com a base de cobertura

## 4. Fontes oficiais da Anatel (planejadas, ainda não integradas)

### Meu Município — Acessos e Cobertura de Telecomunicações
Fonte: Anatel, publicado via dados.gov.br
Tipo: Tabular (CSV), atualização periódica
Granularidade: Município, UF e Região
Variáveis: acessos de banda larga fixa, telefonia móvel, telefonia fixa, TV por assinatura

### Painel de Cobertura Móvel (Anatel)
Tipo: Geoespacial/indicador de presença de sinal (3G/4G) por área
Granularidade: Município/região, por tecnologia e operadora

### Painel de Banda Larga Fixa (Anatel)
Tipo: Tabular, com recortes por faixa de velocidade, tecnologia e empresa
Granularidade: Região, UF e Município

**Observação:** essas três fontes são apresentadas em painéis interativos e podem exigir navegação manual para exportação — a ser resolvido na próxima etapa do projeto. A primeira (dados.gov.br) é a mais provável de oferecer exportação direta em CSV, sendo tratada como fonte prioritária para a integração futura.

## Qualidade e limitações gerais

- A base de cobertura atual é sintética/reduzida — não deve ser usada como fonte de conclusões reais sobre desigualdade de infraestrutura, apenas como demonstração técnica
- O scraping depende da estrutura HTML do Teletime no momento da coleta; mudanças no site podem exigir ajuste nos seletores
- Dados enviados por upload não passam por validação de qualidade automatizada
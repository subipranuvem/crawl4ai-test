# Crawl4AI Scraper

Este repositório contém códigos para coleta de dados utilizando a biblioteca **Crawl4AI**, abordando diferentes métodos de extração.

## Instalação

Antes de executar os scripts, instale as dependências e configure o ambiente:

```bash
pip install crawl4ai && \
crawl4ai-setup && \
crawl4ai-doctor
```

## Modos de Execução

O repositório oferece três formas de executar o scraper:

### 1. Extração via XPath
Executa o scraper utilizando **XPath** para extrair os dados estruturados.

```bash
python app.py
```

### 2. Extração do Conteúdo em Markdown
Obtém o conteúdo da página em formato **Markdown**.

```bash
python app_simple.py
```

### 3. Extração via LLM (Google Gemini)
Realiza a extração de dados utilizando um **provedor de LLM**, no caso o **Gemini**.

```bash
python app_llm.py
```

> **Importante:** Para utilizar o **Gemini**, substitua `<your_token>` pelo seu token de API no arquivo correspondente.
>
> - Obtenha sua chave de API aqui: [Criar chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br)
> - Consulte as cotas gratuitas aqui: [Preços e limites](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br)

## Artigo Relacionado
Este repositório faz parte do artigo onde detalho minha experiência com o **Crawl4AI**.
Confira o artigo completo aqui: [Link para o artigo]().


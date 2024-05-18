# Tech News (Trybe Project)

The Project consults on technology news. News can be obtained by scraping Trybe's blog.

🚵 Worked Skills:

- Use the interactive Python terminal
- Write your own modules and import them into other codes
- Apply data scraping techniques
- Extract data from HTML content
- Store the data obtained in a database

<details>
    <summary><strong>Portuguese Description</strong></summary></br>

    O Projeto faz consultas em notícias sobre tecnologia. As notícias podem ser obtidas através da raspagem do blog da Trybe.

    🚵 Habilidades trabalhadas:

    - Utilizar o terminal interativo do Python
    - Escrever seus próprios módulos e importá-los em outros códigos
    - Aplicar técnicas de raspagem de dados
    - Extrair dados de conteúdo HTML
    - Armazenar os dados obtidos em um banco de dados
</details>

<br>

<details>
    <summary><strong>How to run</strong></summary></br>

    1. Clone this repository with:

        - `git clone git@github.com:NyPadilha/tech-news.git`
        - `cd  tech-news`

    Using Venv:

        1. Create the Virtual Environment:

            - `python3 -m venv .venv && source .venv/bin/activate`

        2. Install the dependencies:

            - `python3 -m pip install -r dev-requirements.txt`

    Without Venv:

        1. Install dependencies with:

            - `python3 -m pip install -r dev-requirements.txt`

    MongoDB with Docker:

        - `docker compose up -d mongodb`

    Run the project(CLI):

        - `tech-news-analyzer`
</details>

<br>

## What I Coded

- tech_news/scraper.py
- tech_news/analyzer/search_engine.py

## What Trybe Coded

- Basically everything else
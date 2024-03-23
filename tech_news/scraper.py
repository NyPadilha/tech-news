import requests
from bs4 import BeautifulSoup
import time


# Requisito 1
def fetch(url):
    try:
        res = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        time.sleep(1)

        if res.status_code == 200:
            return res.text
        else:
            return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    links = []

    for article in soup.find_all("article", {"class": "entry-preview"}):
        links.append(article.find("a", href=True)["href"])

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError

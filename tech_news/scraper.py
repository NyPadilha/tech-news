import requests
from bs4 import BeautifulSoup
import time
import re
from tech_news.database import create_news


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
    soup = BeautifulSoup(html_content, "html.parser")

    try:
        next_page = soup.find("a", {"class": "next"}, href=True)["href"]
        return next_page
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.find("link", {"rel": "canonical"})["href"]
    title = soup.find("h1", {"class": "entry-title"}).text.strip()
    timestamp = soup.find("li", {"class": "meta-date"}).text
    writer = soup.find("span", {"class": "author"}).a.text
    reading_time = int(
        re.search(
            r"\d+", soup.find("li", {"class": "meta-reading-time"}).text
        ).group()
    )
    summary = soup.find("div", {"class": "entry-content"}).p.text.strip()
    category = soup.find("span", {"class": "label"}).text.strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    data = []
    URL = "https://blog.betrybe.com/"

    while len(data) < amount:
        res = fetch(URL)
        links = scrape_updates(res)

        for link in links:
            news_content = fetch(link)
            data.append(scrape_news(news_content))

            if len(data) == amount:
                break

        if len(data) < amount:
            URL = scrape_next_page_link(res)

    create_news(data)
    return data

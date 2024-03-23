from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    try:
        query = db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            projection=["title", "url"],
        )

        return [(item["title"], item["url"]) for item in query]

    except Exception as e:
        raise e


def format_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_date(date):
    formated_date = format_date(date)

    try:
        query = db.news.find(
            {"timestamp": formated_date},
            projection=["title", "url"],
        )

        return [(item["title"], item["url"]) for item in query]

    except Exception as e:
        raise e


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError

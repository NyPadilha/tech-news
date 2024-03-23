from tech_news.database import db


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


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError

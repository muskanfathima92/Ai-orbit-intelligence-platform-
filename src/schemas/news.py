from src.models import Entity


class NewsArticle(Entity):
    entity_type: str = "news"
    published_at: str | None = None
    author: str | None = None
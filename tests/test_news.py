from src.discovery.news import news_to_entity


def test_news_to_entity():

    article = {
        "title": "AI Technology News",
        "description": "Latest artificial intelligence news",
        "url": "https://example.com/article",
        "published_at": "2026-08-18",
        "author": "Test Author",
        "source_name": "Test RSS",
        "source_url": "https://example.com/rss",
    }

    entity = news_to_entity(article)

    assert entity.entity_type == "news"
    assert entity.name == "AI Technology News"
    assert str(entity.url) == "https://example.com/article"
    assert entity.author == "Test Author"
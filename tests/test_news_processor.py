from src.processing.news_processor import process_news_data


def test_process_news_data():

    news = process_news_data()

    assert isinstance(news, list)
    assert len(news) > 0

    first = news[0]

    assert first["entity_type"] == "news"
    assert first["name"]
    assert first["url"]
    assert first["source"]
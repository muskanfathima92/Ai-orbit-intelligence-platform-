import json
from pathlib import Path
from typing import Any

import feedparser

from src.schemas import NewsArticle


RSS_FEEDS = {
    "Google AI News": "https://news.google.com/rss/search?q=artificial+intelligence",
}


def fetch_news(
    limit: int = 20
) -> list[dict[str, Any]]:

    records = []

    for source_name, feed_url in RSS_FEEDS.items():

        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:limit]:

            records.append({
                "title": entry.get("title", ""),
                "description": entry.get(
                    "summary",
                    ""
                ),
                "url": entry.get("link"),
                "published_at": entry.get(
                    "published",
                    None
                ),
                "author": entry.get(
                    "author",
                    None
                ),
                "source_name": source_name,
                "source_url": feed_url,
            })

    return records


def news_to_entity(
    article: dict[str, Any]
) -> NewsArticle:

    return NewsArticle(
        name=article.get(
            "title",
            "Untitled"
        ),
        description=article.get(
            "description",
            ""
        ),
        url=article.get("url"),
        categories=[
            "ai",
            "news"
        ],
        source={
            "name": article.get(
                "source_name",
                "RSS"
            ),
            "url": article.get(
                "source_url"
            ),
        },
        published_at=article.get(
            "published_at"
        ),
        author=article.get(
            "author"
        ),
    )


def save_raw_news(
    records: list[dict[str, Any]]
) -> str:

    output_dir = Path("data/raw")
    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = output_dir / "news.json"

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            records,
            file,
            indent=2,
            ensure_ascii=False
        )

    return str(output_file)
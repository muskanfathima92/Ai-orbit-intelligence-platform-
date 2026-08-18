import json
from pathlib import Path

from src.discovery.news import news_to_entity


def process_news_data(
    input_file: str = "data/raw/news.json",
    output_file: str = "data/processed/news.json"
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", encoding="utf-8") as file:
        raw_news = json.load(file)

    entities = []

    for article in raw_news:
        entity = news_to_entity(article)
        entities.append(entity.model_dump(mode="json"))

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            entities,
            file,
            indent=2,
            ensure_ascii=False
        )

    return entities
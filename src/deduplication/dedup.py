from typing import Any


def deduplicate_entities(
    entities: list[dict[str, Any]]
) -> list[dict[str, Any]]:

    seen_urls = set()
    unique_entities = []

    for entity in entities:

        url = entity.get("url")

        if url:
            url = str(url).rstrip("/").lower()

            if url in seen_urls:
                continue

            seen_urls.add(url)

        unique_entities.append(entity)

    return unique_entities
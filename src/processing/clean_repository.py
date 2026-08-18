import json
from pathlib import Path

from src.cleaning.cleaning import (
    clean_text,
    normalize_url,
    clean_categories
)


def clean_repository_data(
    input_file: str = "data/processed/repositories.json",
    output_file: str = "data/processed/repositories_clean.json"
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", encoding="utf-8") as file:
        repositories = json.load(file)

    cleaned = []

    for repo in repositories:

        repo["name"] = clean_text(repo.get("name"))

        repo["description"] = clean_text(
            repo.get("description")
        )

        repo["url"] = normalize_url(
            repo.get("url")
        )

        repo["categories"] = clean_categories(
            repo.get("categories")
        )

        cleaned.append(repo)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            cleaned,
            file,
            indent=2,
            ensure_ascii=False
        )

    return cleaned
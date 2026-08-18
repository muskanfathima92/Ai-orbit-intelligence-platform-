import json
from pathlib import Path

from src.discovery.github import repository_to_entity


def process_github_data(
    input_file: str = "data/raw/github.json",
    output_file: str = "data/processed/repositories.json"
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    entities = []

    for repo in raw_data:
        entity = repository_to_entity(repo)
        entities.append(entity.model_dump(mode="json"))

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            entities,
            file,
            indent=2,
            ensure_ascii=False
        )

    return entities
import json
from pathlib import Path

from src.classification.classifier import classify_entity


def classify_repository_data(
    input_file: str = "data/processed/repositories_dedup.json",
    output_file: str = "data/processed/repositories_classified.json"
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", encoding="utf-8") as file:
        entities = json.load(file)

    for entity in entities:
        entity["entity_type"] = classify_entity(entity)

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
import json
from pathlib import Path

from src.deduplication.dedup import deduplicate_entities


def deduplicate_repository_data(
    input_file: str = "data/processed/repositories_clean.json",
    output_file: str = "data/processed/repositories_dedup.json"
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", encoding="utf-8") as file:
        entities = json.load(file)

    unique_entities = deduplicate_entities(entities)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            unique_entities,
            file,
            indent=2,
            ensure_ascii=False
        )

    return unique_entities
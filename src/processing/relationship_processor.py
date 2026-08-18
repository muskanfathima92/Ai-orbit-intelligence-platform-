import json
from pathlib import Path

from src.relationships.relationship_mapper import map_relationships


def generate_relationships(
    input_file: str = "data/processed/entities.json",
    output_file: str = "data/processed/relationships.json",
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open(
        "r",
        encoding="utf-8"
    ) as file:

        entities = json.load(file)

    relationships = map_relationships(
        entities
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            relationships,
            file,
            indent=2,
            ensure_ascii=False
        )

    return relationships
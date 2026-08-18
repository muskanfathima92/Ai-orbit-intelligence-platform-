import json
from pathlib import Path

from src.discovery.huggingface import model_to_entity


def process_huggingface_data(
    input_file: str = "data/raw/huggingface.json",
    output_file: str = "data/processed/models.json"
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", encoding="utf-8") as file:
        raw_models = json.load(file)

    entities = []

    for model in raw_models:
        entity = model_to_entity(model)
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
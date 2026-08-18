import json
from pathlib import Path

from src.validation.validator import validate_entities


def validate_repository_data(
    input_file: str = "data/processed/repositories_resolved.json",
    output_file: str = "data/processed/validation_report.json",
) -> dict:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", encoding="utf-8") as file:
        entities = json.load(file)

    report = validate_entities(entities)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=2,
            ensure_ascii=False
        )

    return report
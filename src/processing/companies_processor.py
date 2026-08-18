import json
from pathlib import Path

from src.discovery.companies import company_to_entity


def process_companies_data(
    input_file: str = "data/raw/companies.json",
    output_file: str = "data/processed/companies.json"
) -> list[dict]:

    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open(
        "r",
        encoding="utf-8"
    ) as file:

        raw_companies = json.load(file)

    entities = []

    for company in raw_companies:

        entity = company_to_entity(company)

        entities.append(
            entity.model_dump(mode="json")
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
            entities,
            file,
            indent=2,
            ensure_ascii=False
        )

    return entities
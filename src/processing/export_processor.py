import json
from pathlib import Path

import pandas as pd


def export_final_data(
    input_file: str = "data/processed/entities.json",
    json_output: str = "data/final/entities_final.json",
    csv_output: str = "data/final/entities_final.csv",
):

    with open(
        input_file,
        "r",
        encoding="utf-8"
    ) as file:
        entities = json.load(file)

    output_dir = Path("data/final")
    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        json_output,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            entities,
            file,
            indent=2,
            ensure_ascii=False
        )

    rows = []

    for entity in entities:

        row = {
            "id": entity.get("id"),
            "entity_type": entity.get("entity_type"),
            "name": entity.get("name"),
            "description": entity.get("description"),
            "url": entity.get("url"),
            "categories": ", ".join(
                entity.get("categories", [])
            ),
            "source_name": (
                entity.get("source", {})
                .get("name")
            ),
            "source_url": (
                entity.get("source", {})
                .get("url")
            ),
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    df.to_csv(
        csv_output,
        index=False
    )

    return {
        "json": json_output,
        "csv": csv_output,
        "records": len(entities),
    }
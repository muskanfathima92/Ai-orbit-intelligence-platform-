import json
from collections import Counter
from pathlib import Path


def generate_quality_report(
    input_file: str = "data/processed/entities.json",
    output_file: str = "data/processed/quality_report.json",
) -> dict:

    with open(
        input_file,
        "r",
        encoding="utf-8"
    ) as file:
        entities = json.load(file)

    total = len(entities)

    type_counts = Counter(
        entity.get("entity_type")
        for entity in entities
    )

    missing_names = sum(
        not entity.get("name")
        for entity in entities
    )

    missing_sources = sum(
        not entity.get("source")
        for entity in entities
    )

    missing_urls = sum(
        not entity.get("url")
        for entity in entities
    )

    ids = [
        entity.get("id")
        for entity in entities
    ]

    duplicate_ids = (
        len(ids) - len(set(ids))
    )

    report = {
        "total_entities": total,
        "entity_types": dict(type_counts),
        "missing_names": missing_names,
        "missing_sources": missing_sources,
        "missing_urls": missing_urls,
        "duplicate_ids": duplicate_ids,
        "quality_status": (
            "PASS"
            if (
                missing_names == 0
                and missing_sources == 0
                and duplicate_ids == 0
            )
            else "REVIEW"
        ),
    }

    output_path = Path(output_file)

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
            indent=2
        )

    return report
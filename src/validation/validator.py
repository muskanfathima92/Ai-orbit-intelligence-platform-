from typing import Any
from urllib.parse import urlparse


ALLOWED_ENTITY_TYPES = {
    "model",
    "repository",
    "company",
    "tool",
    "mcp",
    "task",
    "news",
    "video",
    "device",
    "robot",
}


def is_valid_url(url: str | None) -> bool:
    if not url:
        return False

    try:
        parsed = urlparse(str(url))
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except Exception:
        return False


def validate_entity(entity: dict[str, Any]) -> list[str]:

    errors = []

    required_fields = [
        "id",
        "entity_type",
        "name",
        "source",
    ]

    for field in required_fields:
        if not entity.get(field):
            errors.append(f"Missing required field: {field}")

    if entity.get("entity_type") not in ALLOWED_ENTITY_TYPES:
        errors.append(
            f"Invalid entity type: {entity.get('entity_type')}"
        )

    if entity.get("url") and not is_valid_url(entity["url"]):
        errors.append("Invalid URL")

    return errors


def validate_entities(
    entities: list[dict[str, Any]]
) -> dict[str, Any]:

    errors = []
    ids = set()
    duplicate_ids = set()

    for entity in entities:

        entity_id = str(entity.get("id", ""))

        if entity_id in ids:
            duplicate_ids.add(entity_id)

        ids.add(entity_id)

        entity_errors = validate_entity(entity)

        if entity_errors:
            errors.append({
                "id": entity_id,
                "errors": entity_errors
            })

    return {
        "valid": len(errors) == 0 and len(duplicate_ids) == 0,
        "total": len(entities),
        "invalid_records": errors,
        "duplicate_ids": list(duplicate_ids),
    }
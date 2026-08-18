import re
from typing import Any


def normalize_name(name: str | None) -> str:
    if not name:
        return ""

    name = name.lower().strip()

    name = re.sub(r"[^a-z0-9]+", " ", name)

    return " ".join(name.split())


def normalize_url(url: str | None) -> str:
    if not url:
        return ""

    return str(url).strip().rstrip("/").lower()


def entity_key(entity: dict[str, Any]) -> str:

    entity_type = entity.get("entity_type", "")

    url = normalize_url(entity.get("url"))

    if url:
        return f"url:{url}"

    name = normalize_name(entity.get("name"))

    return f"name:{entity_type}:{name}"


def resolve_entities(
    entities: list[dict[str, Any]]
) -> list[dict[str, Any]]:

    canonical = {}
    resolved = []

    for entity in entities:

        key = entity_key(entity)

        if key in canonical:
            continue

        canonical[key] = entity
        resolved.append(entity)

    return resolved
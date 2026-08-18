from typing import Any


ENTITY_TYPES = {
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


def classify_entity(entity: dict[str, Any]) -> str:

    entity_type = entity.get("entity_type")

    if entity_type in ENTITY_TYPES:
        return entity_type

    text = " ".join(
        [
            str(entity.get("name", "")),
            str(entity.get("description", "")),
            " ".join(entity.get("categories", [])),
        ]
    ).lower()

    if "mcp" in text:
        return "mcp"

    if "robot" in text:
        return "robot"

    if "model" in text or "llm" in text:
        return "model"

    if "company" in text or "startup" in text:
        return "company"

    if "news" in text:
        return "news"

    if "video" in text:
        return "video"

    if "device" in text:
        return "device"

    if "tool" in text:
        return "tool"

    if "task" in text:
        return "task"

    if "github" in str(entity.get("source", {})).lower():
        return "repository"

    return "tool"
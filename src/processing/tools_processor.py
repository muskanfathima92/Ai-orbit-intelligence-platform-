import json
from pathlib import Path

from src.discovery.tools import tool_to_entity


def process_tools_data(
    input_file: str = "data/raw/tools.json",
    output_file: str = "data/processed/tools.json"
) -> list[dict]:

    with open(input_file, "r", encoding="utf-8") as file:
        raw_tools = json.load(file)

    entities = []

    for tool in raw_tools:
        entity = tool_to_entity(tool)
        entities.append(entity.model_dump(mode="json"))

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            entities,
            file,
            indent=2,
            ensure_ascii=False
        )

    return entities
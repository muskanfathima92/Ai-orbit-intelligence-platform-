import json
import uuid
from pathlib import Path


INPUT = Path(
    "data/tools/results/opentools_test_results.json"
)

OUTPUT = Path(
    "data/tools/results/ai_orbit_tools.json"
)


with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    tools = json.load(f)


formatted_tools = []


for tool in tools:

    record = {
        "id": str(uuid.uuid4()),

        "entity_type": "tool",

        "name": tool.get(
            "name"
        ),

        "description": tool.get(
            "description"
        ),

        "url": tool.get(
            "tool_url"
        ),

        "categories": [],

        "source": {
            "name": "OpenTools",
            "url": tool.get(
                "opentools_url"
            )
        }
    }

    formatted_tools.append(
        record
    )


OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT.write_text(
    json.dumps(
        formatted_tools,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


print(
    f"Formatted {len(formatted_tools)} tools"
)

print(
    "Saved:",
    OUTPUT
)
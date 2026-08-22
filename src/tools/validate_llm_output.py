import json
from pathlib import Path


INPUT = Path(
    "data/tools/results/llm_output.json"
)


REQUIRED = [
    "name",
    "description",
    "url",
    "categories",
    "source"
]


with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    tools = json.load(f)


valid = 0

print("\n========== LLM OUTPUT VALIDATION ==========\n")


for index, tool in enumerate(
    tools,
    start=1
):

    missing = [
        field
        for field in REQUIRED
        if field not in tool
    ]

    if missing:

        print(
            f"{index}. {tool.get('name')} ❌"
        )

        print(
            "Missing:",
            missing
        )

    else:

        valid += 1

        print(
            f"{index}. {tool.get('name')} ✅"
        )


print(
    f"\nValid: {valid}/{len(tools)}"
)
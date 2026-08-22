import json
from pathlib import Path


INPUT = Path(
    "data/tools/results/opentools_test_results.json"
)


REQUIRED_FIELDS = [
    "name",
    "description",
    "opentools_url",
    "tool_url",
    "source"
]


with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    tools = json.load(f)


print("\n========== DATA QUALITY CHECK ==========\n")


for index, tool in enumerate(
    tools,
    start=1
):

    print(
        f"Tool {index}: {tool.get('name')}"
    )

    print(
        f"  OpenTools category: "
        f"{tool.get('category')}"
    )

    print(
        f"  Schema category: "
        f"{tool.get('schema_category')}"
    )

    for field in REQUIRED_FIELDS:

        value = tool.get(field)

        if value:

            print(
                f"  {field}: OK"
            )

        else:

            print(
                f"  {field}: MISSING"
            )

    print()


print(
    "Total tools:",
    len(tools)
)
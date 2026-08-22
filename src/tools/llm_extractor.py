import json
from pathlib import Path


INPUT = Path(
    "data/tools/results/opentools_test_results.json"
)

OUTPUT = Path(
    "data/tools/results/llm_input.json"
)


def build_llm_input(tool):

    return {
        "source": {
            "name": "OpenTools",
            "url": tool.get("opentools_url")
        },

        "tool_data": {
            "name": tool.get("name"),
            "description": tool.get("description"),
            "url": tool.get("tool_url"),
            "category": tool.get("category"),
            "keywords": tool.get("keywords")
        }
    }


# -----------------------------
# LOAD SCRAPED DATA
# -----------------------------

with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    tools = json.load(f)


# -----------------------------
# PREPARE LLM INPUT
# -----------------------------

llm_inputs = []

for tool in tools:

    llm_inputs.append(
        build_llm_input(tool)
    )


# -----------------------------
# SAVE
# -----------------------------

OUTPUT.write_text(
    json.dumps(
        llm_inputs,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


print(
    f"Prepared {len(llm_inputs)} tools"
)

print(
    "Saved:",
    OUTPUT
)
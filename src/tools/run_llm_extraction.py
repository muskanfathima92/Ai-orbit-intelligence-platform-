import json
from pathlib import Path

from prompts import SYSTEM_PROMPT
from mock_llm import MockLLMClient


INPUT = Path(
    "data/tools/results/llm_input.json"
)

OUTPUT = Path(
    "data/tools/results/llm_output.json"
)


# -----------------------------
# LOAD INPUT
# -----------------------------

with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    tools = json.load(f)


client =MockLLMClient()

results = []


# -----------------------------
# PROCESS TOOLS
# -----------------------------

for index, tool in enumerate(
    tools,
    start=1
):

    print(
        f"\n[{index}/{len(tools)}] "
        f"{tool['tool_data']['name']}"
    )

    user_prompt = json.dumps(
        tool,
        indent=2,
        ensure_ascii=False
    )

    try:

        result = client.extract(
            SYSTEM_PROMPT,
            user_prompt
        )

        results.append(result)

        print("SUCCESS")

    except Exception as e:

        print(
            "ERROR:",
            e
        )


# -----------------------------
# SAVE RESULTS
# -----------------------------

OUTPUT.write_text(
    json.dumps(
        results,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


print(
    f"\nSaved {len(results)} results"
)

print(
    "Output:",
    OUTPUT
)
import json
from pathlib import Path


SCRAPED_FILE = Path(
    "data/tools/results/opentools_test_results.json"
)

LLM_FILE = Path(
    "data/tools/results/llm_output.json"
)


with open(
    SCRAPED_FILE,
    "r",
    encoding="utf-8"
) as f:

    scraped = json.load(f)


with open(
    LLM_FILE,
    "r",
    encoding="utf-8"
) as f:

    llm_results = json.load(f)


print(
    "\n========== SCRAPER vs LLM ==========\n"
)


for index, (source, llm) in enumerate(
    zip(scraped, llm_results),
    start=1
):

    print(
        f"\nTool {index}: {source.get('name')}"
    )

    # Name
    if source.get("name") == llm.get("name"):

        print(
            "  Name: MATCH ✅"
        )

    else:

        print(
            "  Name: MISMATCH ❌"
        )

        print(
            "    Scraper:",
            source.get("name")
        )

        print(
            "    LLM:",
            llm.get("name")
        )


    # URL
    if source.get("tool_url") == llm.get("url"):

        print(
            "  URL: MATCH ✅"
        )

    else:

        print(
            "  URL: MISMATCH ❌"
        )

        print(
            "    Scraper:",
            source.get("tool_url")
        )

        print(
            "    LLM:",
            llm.get("url")
        )


    # Source
    if (
        llm.get("source", {}).get("name")
        == "OpenTools"
    ):

        print(
            "  Source: MATCH ✅"
        )

    else:

        print(
            "  Source: CHECK ❌"
        )
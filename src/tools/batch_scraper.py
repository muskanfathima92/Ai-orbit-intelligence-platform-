import json
from pathlib import Path

from scraper import scrape_tool


INPUT = Path(
    "data/tools/opentools_test_urls.json"
)

OUTPUT = Path(
    "data/tools/results"
)

OUTPUT.mkdir(
    parents=True,
    exist_ok=True
)


with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:
    urls = json.load(f)


results = []

for index, url in enumerate(
    urls,
    start=1
):

    print(
        f"\n[{index}/{len(urls)}] Scraping:"
    )

    print(url)

    try:

        data = scrape_tool(url)

        if data:

            results.append(data)

            print(
                "SUCCESS:",
                data["name"]
            )

        else:

            print(
                "FAILED: No tool data found"
            )

    except Exception as e:

        print(
            "ERROR:",
            e
        )


output_file = (
    OUTPUT / "opentools_test_results.json"
)


output_file.write_text(
    json.dumps(
        results,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


print(
    f"\nCompleted: {len(results)} tools"
)

print(
    "Saved:",
    output_file
)
import json
from pathlib import Path
from urllib.parse import urlparse


INPUT = Path(
    "data/tools/results/ai_orbit_tools.json"
)

OUTPUT = Path(
    "data/tools/results/ai_orbit_tools_deduplicated.json"
)


def normalize_url(url):
    """Normalize URL for duplicate checking."""

    if not url:
        return None

    url = url.strip().lower()

    parsed = urlparse(url)

    # Remove www.
    domain = parsed.netloc.replace(
        "www.",
        ""
    )

    # Remove trailing slash
    path = parsed.path.rstrip("/")

    return f"{domain}{path}"


# --------------------------------
# LOAD DATA
# --------------------------------

with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    tools = json.load(f)


# --------------------------------
# REMOVE DUPLICATES
# --------------------------------

unique_tools = []
seen_urls = set()

duplicates = []


for tool in tools:

    url = tool.get("url")

    normalized = normalize_url(
        url
    )

    if not normalized:

        # Keep records that don't have URL
        unique_tools.append(tool)
        continue

    if normalized in seen_urls:

        duplicates.append(tool)

    else:

        seen_urls.add(normalized)
        unique_tools.append(tool)


# --------------------------------
# SAVE RESULT
# --------------------------------

OUTPUT.write_text(
    json.dumps(
        unique_tools,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


# --------------------------------
# REPORT
# --------------------------------

print("\n========== DEDUPLICATION ==========\n")

print(
    "Original tools:",
    len(tools)
)

print(
    "Unique tools:",
    len(unique_tools)
)

print(
    "Duplicates:",
    len(duplicates)
)

print(
    "\nSaved:",
    OUTPUT
)


if duplicates:

    print("\nDuplicate records:")

    for tool in duplicates:

        print(
            "-",
            tool.get("name"),
            "|",
            tool.get("url")
        )
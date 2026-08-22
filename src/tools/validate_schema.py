import json
from pathlib import Path


# --------------------------------
# INPUT FILE
# --------------------------------

INPUT = Path(
    "data/tools/results/ai_orbit_tools_deduplicated.json"
)


# --------------------------------
# REQUIRED FIELDS
# --------------------------------

REQUIRED_FIELDS = [
    "id",
    "entity_type",
    "name",
    "description",
    "url",
    "categories",
    "source"
]


# --------------------------------
# LOAD JSON
# --------------------------------

if not INPUT.exists():

    print(
        f"ERROR: File not found: {INPUT}"
    )

    raise SystemExit(1)


try:

    with open(
        INPUT,
        "r",
        encoding="utf-8"
    ) as f:

        tools = json.load(f)

except json.JSONDecodeError as e:

    print(
        "ERROR: Invalid JSON file."
    )

    print(e)

    raise SystemExit(1)


# --------------------------------
# CHECK JSON STRUCTURE
# --------------------------------

if not isinstance(tools, list):

    print(
        "ERROR: Expected a JSON list of tools."
    )

    raise SystemExit(1)


# --------------------------------
# VALIDATION
# --------------------------------

print(
    "\n========== AI ORBIT SCHEMA VALIDATION ==========\n"
)


valid_count = 0
invalid_count = 0


for index, tool in enumerate(
    tools,
    start=1
):

    name = tool.get(
        "name",
        "Unknown"
    )

    errors = []


    # -----------------------------
    # Required fields
    # -----------------------------

    for field in REQUIRED_FIELDS:

        if field not in tool:

            errors.append(
                f"Missing field: {field}"
            )


    # -----------------------------
    # Name validation
    # -----------------------------

    if not isinstance(
        tool.get("name"),
        str
    ) or not tool.get("name").strip():

        errors.append(
            "name must be a non-empty string"
        )


    # -----------------------------
    # Description validation
    # -----------------------------

    if not isinstance(
        tool.get("description"),
        str
    ) or not tool.get("description").strip():

        errors.append(
            "description must be a non-empty string"
        )


    # -----------------------------
    # URL validation
    # -----------------------------

    if not isinstance(
        tool.get("url"),
        str
    ) or not tool.get("url").startswith(
        ("http://", "https://")
    ):

        errors.append(
            "url must be a valid HTTP/HTTPS URL"
        )


    # -----------------------------
    # Entity type validation
    # -----------------------------

    if tool.get(
        "entity_type"
    ) != "tool":

        errors.append(
            'entity_type must be "tool"'
        )


    # -----------------------------
    # Categories validation
    # -----------------------------

    if not isinstance(
        tool.get("categories"),
        list
    ):

        errors.append(
            "categories must be a list"
        )

    else:

        for category in tool["categories"]:

            if not isinstance(
                category,
                str
            ):

                errors.append(
                    "Every category must be a string"
                )


    # -----------------------------
    # Source validation
    # -----------------------------

    source = tool.get(
        "source"
    )

    if not isinstance(
        source,
        dict
    ):

        errors.append(
            "source must be an object"
        )

    else:

        if not source.get("name"):

            errors.append(
                "source.name is missing"
            )

        if not source.get("url"):

            errors.append(
                "source.url is missing"
            )

        elif not source["url"].startswith(
            ("http://", "https://")
        ):

            errors.append(
                "source.url must be a valid URL"
            )


    # -----------------------------
    # RESULT
    # -----------------------------

    if errors:

        invalid_count += 1

        print(
            f"Tool {index}: {name} ❌"
        )

        for error in errors:

            print(
                f"   - {error}"
            )

    else:

        valid_count += 1

        print(
            f"Tool {index}: {name} ✅"
        )


# --------------------------------
# FINAL SUMMARY
# --------------------------------

print(
    "\n========== SUMMARY ==========\n"
)

print(
    "Total tools:",
    len(tools)
)

print(
    "Valid tools:",
    valid_count
)

print(
    "Invalid tools:",
    invalid_count
)


if invalid_count == 0:

    print(
        "\n✅ ALL TOOLS PASSED SCHEMA VALIDATION"
    )

else:

    print(
        "\n⚠️ SOME TOOLS FAILED SCHEMA VALIDATION"
    )
import json
import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_tool(url):

    # -----------------------------
    # 1. DOWNLOAD PAGE
    # -----------------------------

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    # -----------------------------
    # 2. PARSE HTML
    # -----------------------------

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # -----------------------------
    # 3. EXTRACT OPENTOOLS CATEGORY
    # -----------------------------

    category = None

    # Look for common category labels.
    # We first check the visible page text.
    possible_categories = [
        "Utilities",
        "Productivity",
        "Developer Tools",
        "Design",
        "Marketing",
        "Writing",
        "Education",
        "Business",
        "Research",
        "Image",
        "Video",
        "Audio"
    ]

    for category_name in possible_categories:

        element = soup.find(
            string=lambda s:
            s and s.strip() == category_name
        )

        if element:

            category = category_name
            break

    # -----------------------------
    # 4. FIND JSON-LD
    # -----------------------------

    scripts = soup.find_all(
        "script",
        type="application/ld+json"
    )

    tool_data = None

    for script in scripts:

        try:

            if not script.string:
                continue

            data = json.loads(
                script.string
            )

            if not isinstance(
                data,
                dict
            ):
                continue

            # JSON-LD with @graph
            if "@graph" in data:

                for item in data["@graph"]:

                    item_type = item.get(
                        "@type",
                        []
                    )

                    if isinstance(
                        item_type,
                        str
                    ):
                        item_type = [
                            item_type
                        ]

                    if (
                        "SoftwareApplication"
                        in item_type
                        or
                        "Product"
                        in item_type
                    ):

                        tool_data = item
                        break

            # Direct JSON-LD object
            else:

                item_type = data.get(
                    "@type",
                    []
                )

                if isinstance(
                    item_type,
                    str
                ):
                    item_type = [
                        item_type
                    ]

                if (
                    "SoftwareApplication"
                    in item_type
                    or
                    "Product"
                    in item_type
                ):

                    tool_data = data

            if tool_data:
                break

        except (
            json.JSONDecodeError,
            TypeError
        ):

            continue

    # -----------------------------
    # 5. CHECK DATA
    # -----------------------------

    if not tool_data:

        return None

    # -----------------------------
    # 6. EXTRACT TOOL URL
    # -----------------------------

    tool_url = (
        tool_data.get("installUrl")
        or
        tool_data.get("downloadUrl")
        or
        tool_data.get("url")
    )

    # -----------------------------
    # 7. RETURN STRUCTURED DATA
    # -----------------------------

    return {

        "name": tool_data.get(
            "name"
        ),

        "description": tool_data.get(
            "description"
        ),

        "opentools_url": url,

        "tool_url": tool_url,

        "category": category,

        "schema_category":
            tool_data.get(
                "applicationCategory"
            ),

        "operating_system":
            tool_data.get(
                "operatingSystem"
            ),

        "keywords":
            tool_data.get(
                "keywords"
            ),

        "author":
            tool_data.get(
                "author"
            ),

        "publisher":
            tool_data.get(
                "publisher"
            ),

        "offers":
            tool_data.get(
                "offers"
            ),

        "rating":
            tool_data.get(
                "aggregateRating"
            ),

        "source": {

            "name": "OpenTools",

            "url": url

        }
    }
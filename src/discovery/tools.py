import json
from pathlib import Path
from typing import Any

import requests

from src.schemas import Tool


GITHUB_API = "https://api.github.com/search/repositories"


def search_tools(
    query: str = "AI tool",
    limit: int = 20
) -> list[dict[str, Any]]:

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit,
    }

    response = requests.get(
        GITHUB_API,
        params=params,
        timeout=20,
    )

    response.raise_for_status()

    return response.json().get("items", [])


def tool_to_entity(
    repository: dict[str, Any]
) -> Tool:

    return Tool(
        name=repository.get(
            "full_name",
            repository.get("name", "Unknown Tool")
        ),
        description=repository.get(
            "description"
        ) or "",
        url=repository.get("html_url"),
        categories=[
            "ai",
            "tool",
        ],
        source={
            "name": "GitHub",
            "url": "https://github.com",
        },
    )


def save_raw_tools(
    repositories: list[dict[str, Any]]
) -> str:

    output_dir = Path("data/raw")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = output_dir / "tools.json"

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            repositories,
            file,
            indent=2,
            ensure_ascii=False
        )

    return str(output_file)
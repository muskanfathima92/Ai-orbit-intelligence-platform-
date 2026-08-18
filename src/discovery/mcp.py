import json
from pathlib import Path
from typing import Any

import requests

from src.schemas import MCPServer


GITHUB_API = "https://api.github.com/search/repositories"


def search_mcp_servers(
    query: str = "MCP server",
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


def mcp_to_entity(
    repository: dict[str, Any]
) -> MCPServer:

    name = repository.get(
        "full_name",
        repository.get("name", "Unknown MCP")
    )

    description = repository.get(
        "description"
    ) or ""

    url = repository.get(
        "html_url"
    )

    return MCPServer(
        name=name,
        description=description,
        url=url,
        categories=[
            "ai",
            "mcp",
        ],
        source={
            "name": "GitHub",
            "url": "https://github.com",
        },
        installation_methods=[
            "GitHub"
        ],
        runtime_requirements=[],
    )


def save_raw_mcp(
    repositories: list[dict[str, Any]]
) -> str:

    output_dir = Path("data/raw")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = output_dir / "mcp.json"

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
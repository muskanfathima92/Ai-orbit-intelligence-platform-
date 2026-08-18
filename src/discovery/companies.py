import json
from pathlib import Path
from typing import Any

import requests

from src.schemas import Company


GITHUB_API = "https://api.github.com/search/users"


def search_companies(
    query: str = "AI",
    limit: int = 20
) -> list[dict[str, Any]]:

    params = {
        "q": f"{query} type:org",
        "per_page": limit,
    }

    response = requests.get(
        GITHUB_API,
        params=params,
        timeout=20,
    )

    response.raise_for_status()

    return response.json().get("items", [])


def company_to_entity(
    organization: dict[str, Any]
) -> Company:

    login = organization.get(
        "login",
        "Unknown Company"
    )

    avatar_url = organization.get(
        "html_url"
    )

    return Company(
        name=login,
        description="AI organization discovered through GitHub",
        url=avatar_url,
        categories=[
            "ai",
            "company",
        ],
        source={
            "name": "GitHub",
            "url": "https://github.com",
        },
        founding_year=None,
        industry_sector="Artificial Intelligence",
        headquarters=None,
    )


def save_raw_companies(
    organizations: list[dict[str, Any]]
) -> str:

    output_dir = Path("data/raw")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = output_dir / "companies.json"

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            organizations,
            file,
            indent=2,
            ensure_ascii=False
        )

    return str(output_file)

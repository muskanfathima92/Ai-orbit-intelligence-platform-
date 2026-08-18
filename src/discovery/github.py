import json
import logging
import os
import time
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

from src.schemas import Repository


load_dotenv()

GITHUB_API = "https://api.github.com"

logger = logging.getLogger(__name__)


def get_headers() -> dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AI-Orbit-Pipeline"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def search_repositories(
    query: str = "artificial intelligence",
    per_page: int = 10,
    retries: int = 3
) -> list[dict[str, Any]]:

    url = f"{GITHUB_API}/search/repositories"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page,
    }

    for attempt in range(1, retries + 1):

        try:
            response = requests.get(
                url,
                params=params,
                headers=get_headers(),
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            logger.info(
                "GitHub returned %s repositories",
                len(data.get("items", []))
            )

            return data.get("items", [])

        except requests.RequestException as exc:

            logger.warning(
                "GitHub request failed (attempt %s/%s): %s",
                attempt,
                retries,
                exc
            )

            if attempt == retries:
                logger.error("GitHub request failed after all retries")
                return []

            time.sleep(2 ** (attempt - 1))

    return []


def repository_to_entity(repo: dict[str, Any]) -> Repository:

    return Repository(
        name=repo.get("name", "Unknown"),
        description=repo.get("description") or "",
        url=repo.get("html_url"),
        categories=["ai"],
        source={
            "name": "GitHub",
            "url": "https://github.com"
        },
        stars=repo.get("stargazers_count", 0),
        primary_language=repo.get("language"),
        last_updated=repo.get("updated_at")
    )


def save_raw_repositories(
    repositories: list[dict[str, Any]]
) -> str:

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "github.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(
            repositories,
            file,
            indent=2,
            ensure_ascii=False
        )

    logger.info(
        "Saved %s raw GitHub repositories to %s",
        len(repositories),
        output_file
    )

    return str(output_file)
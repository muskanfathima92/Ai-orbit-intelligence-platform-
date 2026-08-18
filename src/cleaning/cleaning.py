import re
from urllib.parse import urlparse, urlunparse


def clean_text(value: str | None) -> str:
    if not value:
        return ""

    value = re.sub(r"\s+", " ", value)

    return value.strip()


def normalize_url(url: str | None) -> str | None:
    if not url:
        return None

    url = url.strip()

    parsed = urlparse(url)

    if not parsed.scheme:
        return url

    normalized = urlunparse(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            parsed.path.rstrip("/"),
            "",
            parsed.query,
            ""
        )
    )

    return normalized


def clean_categories(categories: list[str] | None) -> list[str]:
    if not categories:
        return []

    cleaned = []

    for category in categories:
        category = clean_text(category).lower()

        if category and category not in cleaned:
            cleaned.append(category)

    return cleaned
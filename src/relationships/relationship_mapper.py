import json
from typing import Any


ALLOWED_RELATIONSHIPS = {
    "develops",
    "hosted_on",
    "integrates_with",
    "implements",
    "owns",
    "related_to",
}


def create_relationship(
    source: dict[str, Any],
    relationship: str,
    target: dict[str, Any],
    evidence: str | None = None,
    confidence: float | None = None,
) -> dict[str, Any]:

    if relationship not in ALLOWED_RELATIONSHIPS:
        raise ValueError(
            f"Unsupported relationship: {relationship}"
        )

    result = {
        "source_id": str(source["id"]),
        "relationship": relationship,
        "target_id": str(target["id"]),
    }

    if evidence is not None:
        result["evidence"] = evidence

    if confidence is not None:
        result["confidence"] = confidence

    return result


def load_github_repositories(
    file_path: str = "data/raw/github.json",
) -> list[dict[str, Any]]:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def map_relationships(
    entities: list[dict[str, Any]]
) -> list[dict[str, Any]]:

    relationships = []

    companies = [
        entity
        for entity in entities
        if entity.get("entity_type") == "company"
    ]

    repositories = [
        entity
        for entity in entities
        if entity.get("entity_type") == "repository"
    ]

    models = [
        entity
        for entity in entities
        if entity.get("entity_type") == "model"
    ]

    # ---------------------------------------------------------
    # Company -> Repository
    # Use raw GitHub owner information as evidence.
    # ---------------------------------------------------------

    github_data = load_github_repositories()

    github_owner_map = {}

    for repo in github_data:

        repo_name = repo.get("name")

        owner = repo.get("owner") or {}

        owner_login = owner.get("login")

        if repo_name and owner_login:

            github_owner_map[
                repo_name.lower()
            ] = owner_login.lower()

    for company in companies:

        company_name = company.get(
            "name",
            ""
        ).strip()

        if not company_name:
            continue

        company_lower = company_name.lower()

        for repository in repositories:

            repo_name = repository.get(
                "name",
                ""
            ).strip()

            owner = github_owner_map.get(
                repo_name.lower()
            )

            if owner == company_lower:

                relationships.append(
                    create_relationship(
                        source=company,
                        relationship="owns",
                        target=repository,
                        evidence=(
                            f"GitHub API identifies "
                            f"'{company_name}' as the owner "
                            f"of repository '{repo_name}'."
                        ),
                        confidence=0.98,
                    )
                )

    # ---------------------------------------------------------
    # Company -> Model
    # Match the model provider with company name.
    # ---------------------------------------------------------

    for company in companies:

        company_name = company.get(
            "name",
            ""
        ).strip().lower()

        if not company_name:
            continue

        for model in models:

            provider = (
                model.get("provider")
                or ""
            ).strip().lower()

            if provider == company_name:

                relationships.append(
                    create_relationship(
                        source=company,
                        relationship="develops",
                        target=model,
                        evidence=(
                            f"Model provider '{provider}' "
                            f"matches company "
                            f"'{company.get('name')}'."
                        ),
                        confidence=0.90,
                    )
                )

    return relationships
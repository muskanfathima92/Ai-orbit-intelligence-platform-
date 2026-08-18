from src.discovery.github import (
    search_repositories,
    repository_to_entity
)


def test_search_repositories():
    results = search_repositories(
        query="artificial intelligence",
        per_page=3
    )

    assert isinstance(results, list)
    assert len(results) <= 3


def test_repository_to_entity():

    raw_repo = {
        "name": "test-ai",
        "description": "Test AI repository",
        "html_url": "https://github.com/example/test-ai",
        "stargazers_count": 500,
        "language": "Python",
        "updated_at": "2026-08-17T10:00:00Z"
    }

    repo = repository_to_entity(raw_repo)

    assert repo.name == "test-ai"
    assert repo.entity_type == "repository"
    assert repo.stars == 500
    assert repo.primary_language == "Python"
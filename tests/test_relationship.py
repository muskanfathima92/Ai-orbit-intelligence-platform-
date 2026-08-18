import pytest

from src.relationships.relationship_mapper import (
    create_relationship,
    map_relationships,
)


def test_create_relationship():

    company = {
        "id": "company-1",
        "entity_type": "company",
        "name": "Example AI",
    }

    model = {
        "id": "model-1",
        "entity_type": "model",
        "name": "Example Model",
    }

    relationship = create_relationship(
        company,
        "develops",
        model
    )

    assert relationship == {
        "source_id": "company-1",
        "relationship": "develops",
        "target_id": "model-1",
    }


def test_invalid_relationship():

    entity1 = {"id": "1"}
    entity2 = {"id": "2"}

    with pytest.raises(ValueError):
        create_relationship(
            entity1,
            "invalid_relation",
            entity2
        )


def test_repository_relationships_are_not_invented():

    repository = {
        "id": "repo-1",
        "entity_type": "repository",
        "name": "AI Project",
    }

    result = map_relationships([repository])

    assert result == []
from src.validation.validator import (
    validate_entity,
    validate_entities,
)


def test_valid_entity():

    entity = {
        "id": "123",
        "entity_type": "repository",
        "name": "Test Repository",
        "description": "AI project",
        "url": "https://github.com/example/test",
        "source": {
            "name": "GitHub",
            "url": "https://github.com"
        }
    }

    assert validate_entity(entity) == []


def test_missing_name():

    entity = {
        "id": "123",
        "entity_type": "repository",
        "name": "",
        "source": {
            "name": "GitHub",
            "url": "https://github.com"
        }
    }

    errors = validate_entity(entity)

    assert "Missing required field: name" in errors


def test_invalid_entity_type():

    entity = {
        "id": "123",
        "entity_type": "something_unknown",
        "name": "Test",
        "source": {
            "name": "Test",
            "url": "https://example.com"
        }
    }

    errors = validate_entity(entity)

    assert any("Invalid entity type" in error for error in errors)


def test_duplicate_ids():

    entities = [
        {
            "id": "1",
            "entity_type": "repository",
            "name": "A",
            "source": {
                "name": "GitHub",
                "url": "https://github.com"
            }
        },
        {
            "id": "1",
            "entity_type": "repository",
            "name": "B",
            "source": {
                "name": "GitHub",
                "url": "https://github.com"
            }
        }
    ]

    result = validate_entities(entities)

    assert result["valid"] is False
    assert "1" in result["duplicate_ids"]
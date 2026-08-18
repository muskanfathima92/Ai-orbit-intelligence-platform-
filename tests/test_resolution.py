from src.entity_resolution.resolver import (
    normalize_name,
    entity_key,
    resolve_entities
)


def test_normalize_name():

    result = normalize_name("OpenAI-GPT Project")

    assert result == "openai gpt project"


def test_same_url():

    entity1 = {
        "entity_type": "repository",
        "name": "Project A",
        "url": "https://github.com/example/project"
    }

    entity2 = {
        "entity_type": "repository",
        "name": "Project A Copy",
        "url": "https://github.com/example/project/"
    }

    assert entity_key(entity1) == entity_key(entity2)


def test_resolve_entities():

    entities = [
        {
            "entity_type": "repository",
            "name": "Project A",
            "url": "https://github.com/example/project"
        },
        {
            "entity_type": "repository",
            "name": "Project A Copy",
            "url": "https://github.com/example/project/"
        },
        {
            "entity_type": "repository",
            "name": "Project B",
            "url": "https://github.com/example/project-b"
        }
    ]

    result = resolve_entities(entities)

    assert len(result) == 2
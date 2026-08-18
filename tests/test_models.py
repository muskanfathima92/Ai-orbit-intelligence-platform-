from src.models import Entity


def test_entity():
    entity = Entity(
        entity_type="tool",
        name="Example AI",
        description="An AI productivity tool",
        url="https://example.com",
        categories=["productivity"],
        source={
            "name": "Example",
            "url": "https://example.com"
        }
    )

    assert entity.name == "Example AI"
    assert entity.entity_type == "tool"
    assert entity.url is not None
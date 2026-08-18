from src.discovery.tools import tool_to_entity


def test_tool_to_entity():

    repository = {
        "full_name": "example/ai-tool",
        "description": "An AI tool",
        "html_url": "https://github.com/example/ai-tool",
    }

    entity = tool_to_entity(repository)

    assert entity.entity_type == "tool"
    assert entity.name == "example/ai-tool"
    assert str(entity.url) == (
        "https://github.com/example/ai-tool"
    )
    assert "tool" in entity.categories
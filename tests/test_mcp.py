from src.discovery.mcp import mcp_to_entity


def test_mcp_to_entity():

    repository = {
        "full_name": "example/mcp-server",
        "description": "An MCP server for AI tools",
        "html_url": "https://github.com/example/mcp-server",
    }

    entity = mcp_to_entity(repository)

    assert entity.entity_type == "mcp"
    assert entity.name == "example/mcp-server"
    assert str(entity.url) == (
        "https://github.com/example/mcp-server"
    )
    assert "mcp" in entity.categories
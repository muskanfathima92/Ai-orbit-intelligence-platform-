from src.classification.classifier import classify_entity


def test_repository_classification():

    entity = {
        "entity_type": "repository",
        "name": "AI Project",
        "description": "Artificial intelligence project"
    }

    assert classify_entity(entity) == "repository"


def test_model_classification():

    entity = {
        "name": "Example LLM",
        "description": "Large language model"
    }

    assert classify_entity(entity) == "model"


def test_mcp_classification():

    entity = {
        "name": "Example MCP Server",
        "description": "MCP server for AI tools"
    }

    assert classify_entity(entity) == "mcp"
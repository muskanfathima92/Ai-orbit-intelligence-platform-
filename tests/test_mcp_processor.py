from src.processing.mcp_processor import process_mcp_data


def test_process_mcp_data():

    entities = process_mcp_data()

    assert isinstance(entities, list)
    assert len(entities) > 0

    first = entities[0]

    assert first["entity_type"] == "mcp"
    assert first["name"]
    assert first["url"]
    assert first["source"]
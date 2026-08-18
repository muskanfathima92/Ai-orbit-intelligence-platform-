from src.processing.github_processor import process_github_data


def test_process_github_data():

    entities = process_github_data()

    assert isinstance(entities, list)
    assert len(entities) > 0

    first = entities[0]

    assert first["entity_type"] == "repository"
    assert "name" in first
    assert "url" in first
    assert "source" in first
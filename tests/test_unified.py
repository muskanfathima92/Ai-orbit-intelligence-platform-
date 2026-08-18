from src.processing.unified_processor import (
    build_unified_dataset
)


def test_build_unified_dataset():

    entities = build_unified_dataset()

    assert isinstance(entities, list)
    assert len(entities) >= 30

    types = {
        entity["entity_type"]
        for entity in entities
    }

    assert "repository" in types
    assert "model" in types
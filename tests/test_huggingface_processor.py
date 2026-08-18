from src.processing.huggingface_processor import (
    process_huggingface_data
)


def test_process_huggingface_data():

    models = process_huggingface_data()

    assert isinstance(models, list)
    assert len(models) > 0

    first = models[0]

    assert first["entity_type"] == "model"
    assert first["name"]
    assert first["url"]
    assert first["source"]
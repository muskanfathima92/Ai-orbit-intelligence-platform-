from src.deduplication.dedup import deduplicate_entities


def test_deduplicate_entities():

    entities = [
        {
            "id": "1",
            "name": "Project A",
            "url": "https://github.com/example/project"
        },
        {
            "id": "2",
            "name": "Project A Duplicate",
            "url": "https://github.com/example/project/"
        },
        {
            "id": "3",
            "name": "Project B",
            "url": "https://github.com/example/project-b"
        }
    ]

    result = deduplicate_entities(entities)

    assert len(result) == 2
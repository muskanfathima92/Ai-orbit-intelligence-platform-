from src.processing.clean_repository import clean_repository_data


def test_clean_repository_data():

    repositories = clean_repository_data()

    assert len(repositories) > 0

    first = repositories[0]

    assert first["name"] == first["name"].strip()
    assert first["url"] == first["url"].strip()
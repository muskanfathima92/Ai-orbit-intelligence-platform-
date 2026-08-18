from src.cleaning.cleaning import (
    clean_text,
    normalize_url,
    clean_categories
)


def test_clean_text():
    result = clean_text("  Artificial   Intelligence \n Platform  ")

    assert result == "Artificial Intelligence Platform"


def test_normalize_url():
    result = normalize_url(
        "HTTPS://GitHub.com/example/project/"
    )

    assert result == "https://github.com/example/project"


def test_clean_categories():

    result = clean_categories(
        ["AI", " Machine Learning ", "AI"]
    )

    assert result == [
        "ai",
        "machine learning"
    ]
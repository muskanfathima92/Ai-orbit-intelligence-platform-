from src.discovery.companies import company_to_entity


def test_company_to_entity():

    organization = {
        "login": "example-ai",
        "html_url": "https://github.com/example-ai",
    }

    entity = company_to_entity(organization)

    assert entity.entity_type == "company"
    assert entity.name == "example-ai"
    assert str(entity.url) == "https://github.com/example-ai"
    assert entity.industry_sector == "Artificial Intelligence"
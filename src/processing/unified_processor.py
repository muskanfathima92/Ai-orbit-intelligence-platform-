import json
from pathlib import Path


def load_json(path: str) -> list[dict]:

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def build_unified_dataset(
    repository_file: str = "data/processed/repositories_resolved.json",
    model_file: str = "data/processed/models.json",
    news_file: str = "data/processed/news.json",
    mcp_file: str = "data/processed/mcp.json",
    tool_file: str = "data/processed/tools.json",
    company_file: str = "data/processed/companies.json",
    output_file: str = "data/processed/entities.json",
) -> list[dict]:

    repositories = load_json(repository_file)
    models = load_json(model_file)
    news = load_json(news_file)
    mcp_servers = load_json(mcp_file)
    tools = load_json(tool_file)
    companies = load_json(company_file)

    entities = (
        repositories
        + models
        + news
        + mcp_servers
        + tools
        + companies
    )

    output_path = Path(output_file)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            entities,
            file,
            indent=2,
            ensure_ascii=False
        )

    return entities
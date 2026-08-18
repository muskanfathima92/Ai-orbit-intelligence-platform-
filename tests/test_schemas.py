from src.schemas import Company, AIModel, Repository, MCPServer, Tool


def test_company():
    company = Company(
        name="Example AI",
        description="AI company",
        url="https://example.com",
        categories=["ai"],
        source={
            "name": "Example",
            "url": "https://example.com"
        },
        founding_year=2020,
        industry_sector="Artificial Intelligence",
        headquarters="Hyderabad"
    )

    assert company.entity_type == "company"
    assert company.founding_year == 2020


def test_model():
    model = AIModel(
        name="Example Model",
        description="AI model",
        url="https://example.com/model",
        categories=["llm"],
        source={
            "name": "Hugging Face",
            "url": "https://huggingface.co"
        },
        license="Apache-2.0",
        modalities=["text"],
        provider="Example"
    )

    assert model.entity_type == "model"
    assert model.provider == "Example"


def test_repository():
    repo = Repository(
        name="Example Repo",
        description="AI repository",
        url="https://github.com/example/repo",
        categories=["ai"],
        source={
            "name": "GitHub",
            "url": "https://github.com"
        },
        stars=100,
        primary_language="Python"
    )

    assert repo.entity_type == "repository"
    assert repo.stars == 100


def test_mcp():
    server = MCPServer(
        name="Example MCP",
        description="MCP server",
        url="https://example.com/mcp",
        categories=["mcp"],
        source={
            "name": "GitHub",
            "url": "https://github.com"
        },
        installation_methods=["npm"],
        runtime_requirements=["Node.js"]
    )

    assert server.entity_type == "mcp"
    assert "npm" in server.installation_methods


def test_tool():
    tool = Tool(
        name="Example Tool",
        description="AI tool",
        url="https://example.com",
        categories=["productivity"],
        source={
            "name": "Official Site",
            "url": "https://example.com"
        }
    )

    assert tool.entity_type == "tool"
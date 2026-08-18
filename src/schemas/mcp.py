from pydantic import Field
from src.models import Entity


class MCPServer(Entity):
    entity_type: str = "mcp"
    installation_methods: list[str] = Field(default_factory=list)
    runtime_requirements: list[str] = Field(default_factory=list)
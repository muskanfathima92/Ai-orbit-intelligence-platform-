from pydantic import Field
from src.models import Entity


class AIModel(Entity):
    entity_type: str = "model"
    license: str | None = None
    modalities: list[str] = Field(default_factory=list)
    provider: str | None = None
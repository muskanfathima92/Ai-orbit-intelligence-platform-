from datetime import datetime
from src.models import Entity


class Repository(Entity):
    entity_type: str = "repository"
    stars: int = 0
    primary_language: str | None = None
    last_updated: datetime | None = None
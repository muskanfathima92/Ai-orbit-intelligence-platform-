from typing import List
from pydantic import BaseModel, HttpUrl, Field
from uuid import UUID, uuid4


class Source(BaseModel):
    name: str
    url: HttpUrl


class Entity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    entity_type: str
    name: str
    description: str = ""
    url: HttpUrl | None = None
    categories: List[str] = []
    source: Source
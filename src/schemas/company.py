from datetime import datetime
from pydantic import BaseModel, Field
from src.models import Entity


class Company(Entity):
    entity_type: str = "company"
    founding_year: int | None = None
    industry_sector: str | None = None
    headquarters: str | None = None
from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class FeeCategory:
    school_id: int
    name_fr: str
    name_en: str
    description_fr: str = ''
    description_en: str = ''
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["FeeCategory"]

from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class School:
    code: str
    name_fr: str
    name_en: str
    phone: str
    email: str
    address: str
    autorization: str
    founder: str
    principal: str
    city: str
    country: str
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["School"]

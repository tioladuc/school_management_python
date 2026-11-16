from dataclasses import dataclass
from datetime import date, datetime

@dataclass(kw_only=True)
class Student:
    code: str
    gov_matricule: str
    first_name: str
    last_name: str
    email: str
    phone: str
    born_at: str
    born_on: date
    gender: str = 'MALE'
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["Student"]

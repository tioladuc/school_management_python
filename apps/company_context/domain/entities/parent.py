from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class Parent:
    code: str
    first_name: str
    last_name: str
    email: str
    phone: str
    profession: str
    gender: str = 'MALE'
    status: str = 'ACTIVE'
    password: str = ''
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["Parent"]

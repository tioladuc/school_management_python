from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class Staff:
    staff_number: str
    first_name: str
    last_name: str
    email: str
    phone: str = ''
    position: str = ''
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["Staff"]

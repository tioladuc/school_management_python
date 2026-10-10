from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Staff:
    id: int | None
    staff_number: str
    first_name: str
    last_name: str
    email: str
    phone: str = ''
    position: str = ''
    status: str = 'ACTIVE'
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

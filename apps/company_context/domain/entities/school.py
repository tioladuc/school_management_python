from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class School:
    id: int | None
    company_id: int
    code: str
    name: str
    city: str
    country: str
    status: str = 'ACTIVE'
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def is_active(self):
        return self.status == 'ACTIVE'

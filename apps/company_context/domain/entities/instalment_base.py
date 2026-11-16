from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class InstalmentBase:
    instalment_id: int
    class_room_id: int
    amount: int
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["InstalmentBase"]

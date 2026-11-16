from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class Payment:
    yearly_student_id: int
    staff_id: int
    deposited_by: str
    amount: int
    payment_date: datetime
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["Payment"]

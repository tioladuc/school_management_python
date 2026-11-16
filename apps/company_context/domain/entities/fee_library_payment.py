from dataclasses import dataclass
from datetime import date, datetime

@dataclass(kw_only=True)
class FeeLibraryPayment:
    fee_library_id: int
    yearly_student_id: int
    paid_by: str
    paid_on: date
    deposited_amount: float
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["FeeLibraryPayment"]

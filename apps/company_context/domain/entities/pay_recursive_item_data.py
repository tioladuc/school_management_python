from dataclasses import dataclass
from datetime import date, datetime

@dataclass(kw_only=True)
class PayRecursiveItemData:
    pay_recursive_item_id: int
    yearly_staff_id: int
    start_period: date
    end_period: date
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["PayRecursiveItemData"]

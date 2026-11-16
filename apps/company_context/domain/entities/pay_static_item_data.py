from dataclasses import dataclass
from datetime import date, datetime

@dataclass(kw_only=True)
class PayStaticItemData:
    pay_static_item_id: int
    yearly_staff_id: int
    date_payment: date
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["PayStaticItemData"]

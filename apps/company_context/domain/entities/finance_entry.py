from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class FinanceEntry:
    finance_item_id: int
    amount: float
    deposit_date: datetime
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["FinanceEntry"]

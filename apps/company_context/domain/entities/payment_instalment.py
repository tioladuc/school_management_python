from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class PaymentInstalment:
    payment_id: int
    base_instalment_id: int
    description: str
    amount: int
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["PaymentInstalment"]

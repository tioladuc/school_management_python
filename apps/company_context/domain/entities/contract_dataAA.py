from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

@dataclass(kw_only=True)
class ContractData:
    contract_id: int
    transaction_type: str
    transaction_date: date
    quantity: Decimal
    unit_price: Decimal
    total_amount: Decimal
    description: str = ''
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["ContractData"]

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass(frozen=True)
class ContractData:
    id: int | None
    contract_id: int
    transaction_type: str
    transaction_date: date
    quantity: Decimal
    unit_price: Decimal
    total_amount: Decimal
    description: str = ''

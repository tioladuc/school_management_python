from dataclasses import dataclass
from decimal import Decimal
from datetime import date

@dataclass(frozen=True)
class ContractDataDto:
    id: int
    contract_id: int
    transaction_type: str
    transaction_date: date
    quantity: Decimal
    unit_price: Decimal
    total_amount: Decimal
    description: str

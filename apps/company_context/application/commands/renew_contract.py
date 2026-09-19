from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class RenewContractCommand:
    contract_id: int
    new_end_date: date

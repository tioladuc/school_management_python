from dataclasses import dataclass
from decimal import Decimal
from datetime import date

@dataclass(frozen=True)
class ContractDto:
    id: int
    company_id: int
    signature_date: date
    company_setup_price: Decimal
    school_setup_price: Decimal
    academic_year_renewal_price: Decimal
    start_date: date
    end_date: date
    status: str
    currency: str

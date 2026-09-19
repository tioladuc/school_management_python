from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass(frozen=True)
class CreateContractCommand:
    company_id: int
    signature_date: date
    company_setup_price: Decimal
    school_setup_price: Decimal
    academic_year_renewal_price: Decimal
    start_date: date
    end_date: date
    currency: str = "CAD"

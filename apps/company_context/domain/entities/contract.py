from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from ..exceptions import BusinessRuleError

@dataclass
class Contract:
    id: int | None
    company_id: int
    signature_date: date
    company_setup_price: Decimal
    school_setup_price: Decimal
    academic_year_renewal_price: Decimal
    start_date: date
    end_date: date
    status: str = 'DRAFT'
    currency: str = 'CAD'

    @property
    def is_active(self):
        return self.status == 'ACTIVE'

    def activate(self):
        if self.start_date > date.today():
            raise BusinessRuleError('Contract cannot be activated before its start date.')
        self.status = 'ACTIVE'

    def suspend(self):
        if self.status == 'TERMINATED':
            raise BusinessRuleError('A terminated contract cannot be suspended.')
        self.status = 'SUSPENDED'

    def terminate(self):
        self.status = 'TERMINATED'

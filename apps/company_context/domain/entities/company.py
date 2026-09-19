from dataclasses import dataclass, field
from datetime import datetime, timezone
from ..exceptions import BusinessRuleError
from ..value_objects.company_code import CompanyCode

@dataclass
class Company:
    id: int | None
    code: CompanyCode
    name: str
    email: str
    phone: str = ''
    address: str = ''
    status: str = 'ACTIVE'
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def activate(self):
        self.status = 'ACTIVE'
        self.updated_at = datetime.now(timezone.utc)

    def suspend(self):
        if self.status == 'TERMINATED':
            raise BusinessRuleError('A terminated company cannot be suspended.')
        self.status = 'SUSPENDED'
        self.updated_at = datetime.now(timezone.utc)

    def deactivate(self):
        self.status = 'TERMINATED'
        self.updated_at = datetime.now(timezone.utc)

    @property
    def is_active(self):
        return self.status == 'ACTIVE'

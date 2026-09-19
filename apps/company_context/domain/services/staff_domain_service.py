from ..rules.company_rules import can_create_staff
from ..exceptions import BusinessRuleError

class StaffDomainService:
    def ensure_staff_creation_allowed(self, company):
        if not can_create_staff(company):
            raise BusinessRuleError('Only an active company can create staff.')

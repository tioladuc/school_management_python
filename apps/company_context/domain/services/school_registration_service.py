from ..rules.company_rules import can_create_school
from ..exceptions import BusinessRuleError

class SchoolRegistrationService:
    def register(self, company, school, contract):
        if not can_create_school(company, contract):
            raise BusinessRuleError('Only an active company with an active contract can create schools.')
        return school

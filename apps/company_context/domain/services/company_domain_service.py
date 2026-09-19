from ..exceptions import BusinessRuleError

class CompanyDomainService:
    @staticmethod
    def ensure_active(company):
        if not company.is_active:
            raise BusinessRuleError('Company must be active.')

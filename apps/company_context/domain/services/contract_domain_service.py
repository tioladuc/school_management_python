from ..exceptions import BusinessRuleError

class ContractDomainService:
    def ensure_active(self, contract):
        if not contract or not contract.is_active:
            raise BusinessRuleError('An active contract is required.')

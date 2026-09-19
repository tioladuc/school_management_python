from .contract_calculation_service import ContractCalculationService
from ..exceptions import BusinessRuleError

class ContractBillingService:
    TRANSACTION_TYPES = {
        'COMPANY_CREATION', 'SCHOOL_CREATION', 'ACADEMIC_YEAR_RENEWAL',
        'CUSTOM_FEE', 'DISCOUNT', 'CREDIT_NOTE',
    }

    def __init__(self):
        self.calculator = ContractCalculationService()

    def bill_school_creation(self, contract, quantity=1):
        self._ensure_billable(contract)
        return self.calculator.calculate(
            contract, 'SCHOOL_CREATION', quantity, contract.school_setup_price,
            'School creation fee',
        )

    def bill_company_creation(self, contract):
        self._ensure_billable(contract)
        return self.calculator.calculate(
            contract, 'COMPANY_CREATION', 1, contract.company_setup_price,
            'Company creation fee',
        )

    def bill_academic_year_renewal(self, contract, quantity=1):
        self._ensure_billable(contract)
        return self.calculator.calculate(
            contract, 'ACADEMIC_YEAR_RENEWAL', quantity,
            contract.academic_year_renewal_price, 'Academic year renewal fee',
        )

    @staticmethod
    def _ensure_billable(contract):
        if not contract or not contract.is_active:
            raise BusinessRuleError('Contract must be active before billing.')

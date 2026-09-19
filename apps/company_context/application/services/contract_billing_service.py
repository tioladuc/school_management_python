from ...domain.services.contract_billing_service import ContractBillingService as DomainBillingService
from ...domain.exceptions import NotFoundError
from ..dto.contract_data_dto import ContractDataDto

class ContractBillingApplicationService:
    def __init__(self, contracts, contract_data): self.contracts, self.contract_data = contracts, contract_data
    def bill_school_creation(self, company_id, quantity=1):
        contract = self.contracts.get_active_for_company(company_id)
        if not contract: raise NotFoundError('No active contract found.')
        data = DomainBillingService().bill_school_creation(contract, quantity)
        return self.to_dto(self.contract_data.save(data))
    def bill_academic_year_renewal(self, company_id, quantity=1):
        contract = self.contracts.get_active_for_company(company_id)
        if not contract: raise NotFoundError('No active contract found.')
        data = DomainBillingService().bill_academic_year_renewal(contract, quantity)
        return self.to_dto(self.contract_data.save(data))
    def history(self, query): return [self.to_dto(d) for d in self.contract_data.list_for_company(query.company_id)]
    @staticmethod
    def to_dto(d): return ContractDataDto(d.id,d.contract_id,d.transaction_type,d.transaction_date,d.quantity,d.unit_price,d.total_amount,d.description)

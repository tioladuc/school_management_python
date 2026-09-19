from ...application.services.contract_billing_service import ContractBillingApplicationService

class AcademicYearRenewedHandler:
    def __init__(self, billing_service): self.billing_service=billing_service
    def handle(self, event):
        return self.billing_service.bill_academic_year_renewal(event.company_id, quantity=1)

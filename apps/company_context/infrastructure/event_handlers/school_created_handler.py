class SchoolCreatedHandler:
    def __init__(self, billing_service): self.billing_service=billing_service
    def handle(self, event): return self.billing_service.bill_school_creation(event.company_id, quantity=1)

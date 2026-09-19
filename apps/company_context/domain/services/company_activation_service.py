class CompanyActivationService:
    def activate(self, company):
        company.activate()
        return company

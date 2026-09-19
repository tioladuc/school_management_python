class CompanySuspensionService:
    def suspend(self, company):
        company.suspend()
        return company

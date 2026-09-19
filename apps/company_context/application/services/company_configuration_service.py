class CompanyConfigurationApplicationService:
    def __init__(self, repository): self.repository=repository
    def get(self, company_id): return self.repository.get_for_company(company_id)
    def update(self, company_id, data): return self.repository.save_for_company(company_id, data)

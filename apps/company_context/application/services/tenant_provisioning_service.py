class TenantProvisioningApplicationService:
    def __init__(self, provisioning): self.provisioning=provisioning
    def provision(self, company_id, company_code): return self.provisioning.provision(company_id, company_code)
    def initialize(self, database_name): return self.provisioning.initialize(database_name)

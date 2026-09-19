class UpdateCompanyUseCase:
    def __init__(self, service): self.service = service
    def execute(self, command): return self.service.update(command)

class RenewContractUseCase:
    def __init__(self, service): self.service = service
    def execute(self, command): return self.service.renew(command)

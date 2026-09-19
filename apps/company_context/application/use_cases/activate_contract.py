class ActivateContractUseCase:
    def __init__(self, service): self.service = service
    def execute(self, command): return self.service.activate(command)

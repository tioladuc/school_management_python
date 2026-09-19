class UpdateContractUseCase:
    def __init__(self, service): self.service = service
    def execute(self, command): return self.service.update(command)

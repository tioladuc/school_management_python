class SuspendContractUseCase:
    def __init__(self, service): self.service = service
    def execute(self, command): return self.service.suspend(command)

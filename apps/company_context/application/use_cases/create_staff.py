class CreateStaffUseCase:
    def __init__(self, service): self.service = service
    def execute(self, command): return self.service.create(command)

class ContractActivationService:
    def activate(self, contract):
        contract.activate()
        return contract

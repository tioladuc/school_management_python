from dataclasses import dataclass

@dataclass(frozen=True)
class ActivateContractCommand:
    contract_id: int

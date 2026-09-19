from dataclasses import dataclass

@dataclass(frozen=True)
class SuspendContractCommand:
    contract_id: int

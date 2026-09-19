from dataclasses import dataclass

@dataclass(frozen=True)
class ContractActivated:
    entity_id: int
    company_id: int

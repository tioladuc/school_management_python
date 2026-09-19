from dataclasses import dataclass

@dataclass(frozen=True)
class ContractSuspended:
    entity_id: int
    company_id: int

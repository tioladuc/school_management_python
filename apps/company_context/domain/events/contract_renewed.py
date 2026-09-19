from dataclasses import dataclass

@dataclass(frozen=True)
class ContractRenewed:
    entity_id: int
    company_id: int

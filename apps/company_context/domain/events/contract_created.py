from dataclasses import dataclass

@dataclass(frozen=True)
class ContractCreated:
    entity_id: int
    company_id: int

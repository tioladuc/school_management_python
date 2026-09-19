from dataclasses import dataclass

@dataclass(frozen=True)
class ContractDataCreated:
    entity_id: int
    company_id: int

from dataclasses import dataclass

@dataclass(frozen=True)
class CompanyActivated:
    entity_id: int
    company_id: int

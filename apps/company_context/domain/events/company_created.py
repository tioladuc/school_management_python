from dataclasses import dataclass

@dataclass(frozen=True)
class CompanyCreated:
    entity_id: int
    company_id: int

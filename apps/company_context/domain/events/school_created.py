from dataclasses import dataclass

@dataclass(frozen=True)
class SchoolCreated:
    entity_id: int
    company_id: int

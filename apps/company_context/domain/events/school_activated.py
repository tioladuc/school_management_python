from dataclasses import dataclass

@dataclass(frozen=True)
class SchoolActivated:
    entity_id: int
    company_id: int

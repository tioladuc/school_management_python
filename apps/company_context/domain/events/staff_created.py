from dataclasses import dataclass

@dataclass(frozen=True)
class StaffCreated:
    entity_id: int
    company_id: int

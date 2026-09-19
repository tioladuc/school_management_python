from dataclasses import dataclass

@dataclass(frozen=True)
class StaffTerminated:
    entity_id: int
    company_id: int

from dataclasses import dataclass

@dataclass(frozen=True)
class SchoolSuspended:
    entity_id: int
    company_id: int

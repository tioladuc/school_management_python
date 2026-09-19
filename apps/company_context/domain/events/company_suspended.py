from dataclasses import dataclass

@dataclass(frozen=True)
class CompanySuspended:
    entity_id: int
    company_id: int

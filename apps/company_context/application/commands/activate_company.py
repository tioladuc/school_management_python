from dataclasses import dataclass

@dataclass(frozen=True)
class ActivateCompanyCommand:
    company_id: int

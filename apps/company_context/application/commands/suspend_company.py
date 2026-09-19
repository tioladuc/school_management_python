from dataclasses import dataclass

@dataclass(frozen=True)
class SuspendCompanyCommand:
    company_id: int

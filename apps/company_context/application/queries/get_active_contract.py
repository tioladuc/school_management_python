from dataclasses import dataclass
@dataclass(frozen=True)
class GetActiveContractQuery:
    company_id: int

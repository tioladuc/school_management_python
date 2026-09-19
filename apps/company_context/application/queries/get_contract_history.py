from dataclasses import dataclass
@dataclass(frozen=True)
class GetContractHistoryQuery:
    company_id: int

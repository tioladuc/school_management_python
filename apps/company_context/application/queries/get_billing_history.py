from dataclasses import dataclass
@dataclass(frozen=True)
class GetBillingHistoryQuery:
    company_id: int

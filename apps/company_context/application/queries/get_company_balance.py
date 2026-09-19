from dataclasses import dataclass
@dataclass(frozen=True)
class GetCompanyBalanceQuery:
    company_id: int

from dataclasses import dataclass
@dataclass(frozen=True)
class GetCompanyQuery:
    company_id: int

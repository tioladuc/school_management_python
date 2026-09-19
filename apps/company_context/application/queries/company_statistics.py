from dataclasses import dataclass
@dataclass(frozen=True)
class CompanyStatisticsQuery:
    company_id: int

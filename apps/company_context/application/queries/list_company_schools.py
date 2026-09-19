from dataclasses import dataclass
@dataclass(frozen=True)
class ListCompanySchoolsQuery:
    company_id: int

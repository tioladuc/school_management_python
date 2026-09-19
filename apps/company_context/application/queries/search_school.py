from dataclasses import dataclass
@dataclass(frozen=True)
class SearchSchoolQuery:
    company_id: int
    search: str = ""

from dataclasses import dataclass
@dataclass(frozen=True)
class SearchStaffQuery:
    company_id: int
    search: str = ""

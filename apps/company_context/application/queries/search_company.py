from dataclasses import dataclass
@dataclass(frozen=True)
class SearchCompanyQuery:
    search: str = ""
    status: str | None = None

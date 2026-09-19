from dataclasses import dataclass

@dataclass(frozen=True)
class SchoolDto:
    id: int
    company_id: int
    code: str
    name: str
    city: str
    country: str
    status: str

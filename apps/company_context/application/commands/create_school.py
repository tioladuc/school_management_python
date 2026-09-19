from dataclasses import dataclass

@dataclass(frozen=True)
class CreateSchoolCommand:
    company_id: int
    code: str
    name: str
    city: str
    country: str

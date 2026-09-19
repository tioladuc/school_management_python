from dataclasses import dataclass

@dataclass(frozen=True)
class UpdateCompanyCommand:
    company_id: int
    name: str
    email: str
    phone: str = ""
    address: str = ""

from dataclasses import dataclass

@dataclass(frozen=True)
class CompanyDto:
    id: int
    code: str
    name: str
    email: str
    phone: str
    address: str
    status: str
    school_count: int = 0

from dataclasses import dataclass

@dataclass(frozen=True)
class CreateCompanyCommand:
    code: str
    name: str
    email: str
    phone: str = ""
    address: str = ""

from dataclasses import dataclass

@dataclass(frozen=True)
class CreateSchoolCommand:
    # id: int
    code: str
    name_fr: str
    name_en: str
    phone: str
    email: str
    address: str
    autorization: str
    founder: str
    principal: str
    city: str
    country: str
    status: str

from dataclasses import dataclass

from apps.company_context.application.dto.company_dto import CompanyDto
from apps.company_context.application.dto.school_dto import SchoolDto

@dataclass(frozen=True)
class UserOutDto:
    id: int
    company_id: int
    staff_number: str
    first_name: str
    last_name: str
    email: str
    phone: str
    profile: str
    position: str
    status: str
    company: CompanyDto
    school: SchoolDto

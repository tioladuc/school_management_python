from dataclasses import dataclass

@dataclass(frozen=True)
class StaffDto:
    id: int
    company_id: int
    staff_number: str
    first_name: str
    last_name: str
    email: str
    phone: str
    position: str
    status: str

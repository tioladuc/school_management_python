from dataclasses import dataclass

@dataclass(frozen=True)
class UpdateStaffCommand:
    staff_id: int
    first_name: str
    last_name: str
    email: str
    phone: str = ""
    position: str = ""

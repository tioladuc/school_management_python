from dataclasses import dataclass
@dataclass(frozen=True)
class GetStaffQuery:
    staff_id: int

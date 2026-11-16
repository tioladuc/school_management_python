from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class YearlyStudent:
    student_id: int
    academic_year_id: int
    class_room_id: int
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["YearlyStudent"]

from dataclasses import dataclass
from datetime import date, datetime

@dataclass(kw_only=True)
class AcademicYear:
    school_id: int
    year: int
    start_date: date
    end_date: date
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["AcademicYear"]

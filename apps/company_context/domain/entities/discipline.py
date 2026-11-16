from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class Discipline:
    yearly_student_id: int
    justified_absence: int
    unjustified_absence: int
    lateness: int
    reserve: int
    notice: int
    blame: int
    exclusion: int
    description: str
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["Discipline"]

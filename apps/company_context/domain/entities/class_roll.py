from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class ClassRoll:
    yearly_student_id: int
    subject_id: int
    start_period: datetime
    end_period: datetime
    duration: float
    teacher_id: int
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["ClassRoll"]

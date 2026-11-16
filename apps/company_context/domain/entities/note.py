from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class Note:
    yearly_student_id: int
    subject_id: int
    assessment_id: int
    mark: float
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["Note"]

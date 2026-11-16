from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class StudentParent:
    student_id: int
    parent_id: int
    relation: str = 'FATHER'
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["StudentParent"]

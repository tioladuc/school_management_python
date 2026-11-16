from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.student_parent import StudentParent


@dataclass(frozen=True)
class StudentParentDto:
    student_id: int
    parent_id: int
    relation: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    id: int | None

    @staticmethod
    def to_domain(m):
        return StudentParent(
            student_id=m.student_id,
            parent_id=m.parent_id,
            relation=m.relation,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return StudentParentDto(
            student_id=m.student_id,
            parent_id=m.parent_id,
            relation=m.relation,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["StudentParentDto"]

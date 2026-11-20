from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.class_roll import ClassRoll


@dataclass(frozen=True)
class ClassRollDto:
    yearly_student_id: int
    subject_id: int
    start_period: datetime
    end_period: datetime
    duration: float
    teacher_id: int
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return ClassRoll(
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            start_period=m.start_period,
            end_period=m.end_period,
            duration=m.duration,
            teacher_id=m.teacher_id,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return ClassRollDto(
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            start_period=m.start_period,
            end_period=m.end_period,
            duration=m.duration,
            teacher_id=m.teacher_id,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["ClassRollDto"]

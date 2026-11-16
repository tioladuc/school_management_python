from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.student_message import StudentMessage


@dataclass(frozen=True)
class StudentMessageDto:
    yearly_student_id: int
    subject_id: int
    start_period: datetime
    end_period: datetime
    subject_fr: str
    subject_en: str
    content_fr: str
    content_en: str
    teacher_id: int
    category: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return StudentMessage(
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            start_period=m.start_period,
            end_period=m.end_period,
            subject_fr=m.subject_fr,
            subject_en=m.subject_en,
            content_fr=m.content_fr,
            content_en=m.content_en,
            teacher_id=m.teacher_id,
            category=m.category,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return StudentMessageDto(
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            start_period=m.start_period,
            end_period=m.end_period,
            subject_fr=m.subject_fr,
            subject_en=m.subject_en,
            content_fr=m.content_fr,
            content_en=m.content_en,
            teacher_id=m.teacher_id,
            category=m.category,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["StudentMessageDto"]

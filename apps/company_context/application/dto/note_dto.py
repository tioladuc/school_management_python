from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.note import Note


@dataclass(frozen=True)
class NoteDto:
    yearly_student_id: int
    subject_id: int
    assessment_id: int
    mark: float
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return Note(
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            assessment_id=m.assessment_id,
            mark=m.mark,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return NoteDto(
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            assessment_id=m.assessment_id,
            mark=m.mark,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["NoteDto"]

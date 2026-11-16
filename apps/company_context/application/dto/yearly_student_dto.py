from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.yearly_student import YearlyStudent


@dataclass(frozen=True)
class YearlyStudentDto:
    student_id: int
    academic_year_id: int
    class_room_id: int
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    id: int | None

    @staticmethod
    def to_domain(m):
        return YearlyStudent(
            student_id=m.student_id,
            academic_year_id=m.academic_year_id,
            class_room_id=m.class_room_id,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return YearlyStudentDto(
            student_id=m.student_id,
            academic_year_id=m.academic_year_id,
            class_room_id=m.class_room_id,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["YearlyStudentDto"]

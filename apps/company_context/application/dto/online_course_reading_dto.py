from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.online_course_reading import OnlineCourseReading


@dataclass(frozen=True)
class OnlineCourseReadingDto:
    online_course_id: int
    yearly_student_id: int
    reading_date: datetime
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return OnlineCourseReading(
            online_course_id=m.online_course_id,
            yearly_student_id=m.yearly_student_id,
            reading_date=m.reading_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return OnlineCourseReadingDto(
            online_course_id=m.online_course_id,
            yearly_student_id=m.yearly_student_id,
            reading_date=m.reading_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["OnlineCourseReadingDto"]

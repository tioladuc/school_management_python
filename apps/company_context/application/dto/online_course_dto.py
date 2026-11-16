from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.online_course import OnlineCourse


@dataclass(frozen=True)
class OnlineCourseDto:
    subject_id: int
    yearly_staff_id: int
    name_fr: str
    name_en: str
    description_fr: str
    description_en: str
    file_path: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return OnlineCourse(
            subject_id=m.subject_id,
            yearly_staff_id=m.yearly_staff_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            file_path=m.file_path,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return OnlineCourseDto(
            subject_id=m.subject_id,
            yearly_staff_id=m.yearly_staff_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            file_path=m.file_path,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["OnlineCourseDto"]

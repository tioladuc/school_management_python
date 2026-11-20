from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.subject import Subject


@dataclass(frozen=True)
class SubjectDto:
    class_room_id: int
    subject_group_id: int
    yearly_staff_id: int
    name_fr: str
    name_en: str
    description_fr: str
    description_en: str
    coeficient: int
    order: int
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return Subject(
            class_room_id=m.class_room_id,
            subject_group_id=m.subject_group_id,
            yearly_staff_id=m.yearly_staff_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            coeficient=m.coeficient,
            order=m.order,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return SubjectDto(
            class_room_id=m.class_room_id,
            subject_group_id=m.subject_group_id,
            yearly_staff_id=m.yearly_staff_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            coeficient=m.coeficient,
            order=m.order,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["SubjectDto"]

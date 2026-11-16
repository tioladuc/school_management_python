from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.book_category import BookCategory


@dataclass(frozen=True)
class BookCategoryDto:
    school_id: int
    name_fr: str
    name_en: str
    description_fr: str
    description_en: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    id: int | None

    @staticmethod
    def to_domain(m):
        return BookCategory(
            school_id=m.school_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return BookCategoryDto(
            school_id=m.school_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["BookCategoryDto"]

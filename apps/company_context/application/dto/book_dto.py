from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.book import Book


@dataclass(frozen=True)
class BookDto:
    book_category_id: int
    name_fr: str
    name_en: str
    description_fr: str
    description_en: str
    author: str
    second_name_fr: str
    second_name_en: str
    published_date: str
    published_by: str
    illustrated_by: str
    keywords: str
    quantity: int
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return Book(
            book_category_id=m.book_category_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            author=m.author,
            second_name_fr=m.second_name_fr,
            second_name_en=m.second_name_en,
            published_date=m.published_date,
            published_by=m.published_by,
            illustrated_by=m.illustrated_by,
            keywords=m.keywords,
            quantity=m.quantity,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return BookDto(
            book_category_id=m.book_category_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            author=m.author,
            second_name_fr=m.second_name_fr,
            second_name_en=m.second_name_en,
            published_date=m.published_date,
            published_by=m.published_by,
            illustrated_by=m.illustrated_by,
            keywords=m.keywords,
            quantity=m.quantity,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["BookDto"]

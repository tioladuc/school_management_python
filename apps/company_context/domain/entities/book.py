from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class Book:
    book_category_id: int
    name_fr: str
    name_en: str
    description_fr: str = ''
    description_en: str = ''
    author: str
    second_name_fr: str
    second_name_en: str
    published_date: str
    published_by: str
    illustrated_by: str
    keywords: str
    quantity: int
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["Book"]

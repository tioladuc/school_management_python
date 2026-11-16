from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.finance_item import FinanceItem


@dataclass(frozen=True)
class FinanceItemDto:
    finance_subcategory_id: int
    code: str
    name_fr: str
    name_en: str
    description_fr: str
    description_en: str
    initial_amount: float
    current_amount: float
    finance_type: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return FinanceItem(
            finance_subcategory_id=m.finance_subcategory_id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            initial_amount=m.initial_amount,
            current_amount=m.current_amount,
            finance_type=m.finance_type,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return FinanceItemDto(
            finance_subcategory_id=m.finance_subcategory_id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            initial_amount=m.initial_amount,
            current_amount=m.current_amount,
            finance_type=m.finance_type,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["FinanceItemDto"]

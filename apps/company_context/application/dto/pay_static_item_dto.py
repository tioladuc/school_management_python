from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.pay_static_item import PayStaticItem


@dataclass(frozen=True)
class PayStaticItemDto:
    pay_category_id: int
    code: str
    name_fr: str
    name_en: str
    description_fr: str
    description_en: str
    order: int
    type_choice: str
    calculation_choice: str
    value: float
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return PayStaticItem(
            pay_category_id=m.pay_category_id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            order=m.order,
            type_choice=m.type_choice,
            calculation_choice=m.calculation_choice,
            value=m.value,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return PayStaticItemDto(
            pay_category_id=m.pay_category_id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            order=m.order,
            type_choice=m.type_choice,
            calculation_choice=m.calculation_choice,
            value=m.value,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["PayStaticItemDto"]

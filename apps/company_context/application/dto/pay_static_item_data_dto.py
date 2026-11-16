from dataclasses import dataclass
from datetime import date, datetime

from apps.company_context.domain.entities.pay_static_item_data import PayStaticItemData


@dataclass(frozen=True)
class PayStaticItemDataDto:
    pay_static_item_id: int
    yearly_staff_id: int
    date_payment: date
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return PayStaticItemData(
            pay_static_item_id=m.pay_static_item_id,
            yearly_staff_id=m.yearly_staff_id,
            date_payment=m.date_payment,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return PayStaticItemDataDto(
            pay_static_item_id=m.pay_static_item_id,
            yearly_staff_id=m.yearly_staff_id,
            date_payment=m.date_payment,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["PayStaticItemDataDto"]

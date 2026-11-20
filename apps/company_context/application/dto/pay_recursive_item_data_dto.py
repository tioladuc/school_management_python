from dataclasses import dataclass
from datetime import date, datetime

from apps.company_context.domain.entities.pay_recursive_item_data import PayRecursiveItemData


@dataclass(frozen=True)
class PayRecursiveItemDataDto:
    pay_recursive_item_id: int
    yearly_staff_id: int
    start_period: date
    end_period: date
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return PayRecursiveItemData(
            pay_recursive_item_id=m.pay_recursive_item_id,
            yearly_staff_id=m.yearly_staff_id,
            start_period=m.start_period,
            end_period=m.end_period,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return PayRecursiveItemDataDto(
            pay_recursive_item_id=m.pay_recursive_item_id,
            yearly_staff_id=m.yearly_staff_id,
            start_period=m.start_period,
            end_period=m.end_period,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["PayRecursiveItemDataDto"]

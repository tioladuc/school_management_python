from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.finance_entry import FinanceEntry


@dataclass(frozen=True)
class FinanceEntryDto:
    finance_item_id: int
    amount: float
    deposit_date: datetime
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return FinanceEntry(
            finance_item_id=m.finance_item_id,
            amount=m.amount,
            deposit_date=m.deposit_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return FinanceEntryDto(
            finance_item_id=m.finance_item_id,
            amount=m.amount,
            deposit_date=m.deposit_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["FinanceEntryDto"]

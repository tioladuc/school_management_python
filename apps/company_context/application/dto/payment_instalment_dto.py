from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.payment_instalment import PaymentInstalment


@dataclass(frozen=True)
class PaymentInstalmentDto:
    payment_id: int
    base_instalment_id: int
    description: str
    amount: int
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return PaymentInstalment(
            payment_id=m.payment_id,
            base_instalment_id=m.base_instalment_id,
            description=m.description,
            amount=m.amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return PaymentInstalmentDto(
            payment_id=m.payment_id,
            base_instalment_id=m.base_instalment_id,
            description=m.description,
            amount=m.amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["PaymentInstalmentDto"]

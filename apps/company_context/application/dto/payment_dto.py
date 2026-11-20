from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.payment import Payment


@dataclass(frozen=True)
class PaymentDto:
    yearly_student_id: int
    staff_id: int
    deposited_by: str
    amount: int
    payment_date: datetime
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return Payment(
            yearly_student_id=m.yearly_student_id,
            staff_id=m.staff_id,
            deposited_by=m.deposited_by,
            amount=m.amount,
            payment_date=m.payment_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return PaymentDto(
            yearly_student_id=m.yearly_student_id,
            staff_id=m.staff_id,
            deposited_by=m.deposited_by,
            amount=m.amount,
            payment_date=m.payment_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["PaymentDto"]

from dataclasses import dataclass
from datetime import date, datetime

from apps.company_context.domain.entities.fee_online_course_payment import FeeOnlineCoursePayment


@dataclass(frozen=True)
class FeeOnlineCoursePaymentDto:
    fee_online_course_id: int
    yearly_student_id: int
    paid_by: str
    paid_on: date
    deposited_amount: float
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return FeeOnlineCoursePayment(
            fee_online_course_id=m.fee_online_course_id,
            yearly_student_id=m.yearly_student_id,
            paid_by=m.paid_by,
            paid_on=m.paid_on,
            deposited_amount=m.deposited_amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return FeeOnlineCoursePaymentDto(
            fee_online_course_id=m.fee_online_course_id,
            yearly_student_id=m.yearly_student_id,
            paid_by=m.paid_by,
            paid_on=m.paid_on,
            deposited_amount=m.deposited_amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["FeeOnlineCoursePaymentDto"]

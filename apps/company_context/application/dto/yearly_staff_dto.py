from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.yearly_staff import YearlyStaff


@dataclass(frozen=True)
class YearlyStaffDto:
    academic_year_id: int
    staff_id: int
    profile: str
    payment_type: str
    fixed_amount: float
    hour_amount: float
    hour_sup_15_amount: float
    hour_sup_20_amount: float
    hour_sup_30_amount: float
    hour_sup_40_amount: float
    hour_sup_50_amount: float
    day_amount: float
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return YearlyStaff(
            academic_year_id=m.academic_year_id,
            staff_id=m.staff_id,
            profile=m.profile,
            payment_type=m.payment_type,
            fixed_amount=m.fixed_amount,
            hour_amount=m.hour_amount,
            hour_sup_15_amount=m.hour_sup_15_amount,
            hour_sup_20_amount=m.hour_sup_20_amount,
            hour_sup_30_amount=m.hour_sup_30_amount,
            hour_sup_40_amount=m.hour_sup_40_amount,
            hour_sup_50_amount=m.hour_sup_50_amount,
            day_amount=m.day_amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return YearlyStaffDto(
            academic_year_id=m.academic_year_id,
            staff_id=m.staff_id,
            profile=m.profile,
            payment_type=m.payment_type,
            fixed_amount=m.fixed_amount,
            hour_amount=m.hour_amount,
            hour_sup_15_amount=m.hour_sup_15_amount,
            hour_sup_20_amount=m.hour_sup_20_amount,
            hour_sup_30_amount=m.hour_sup_30_amount,
            hour_sup_40_amount=m.hour_sup_40_amount,
            hour_sup_50_amount=m.hour_sup_50_amount,
            day_amount=m.day_amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["YearlyStaffDto"]

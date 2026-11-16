from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class YearlyStaff:
    academic_year_id: int
    staff_id: int
    profile: str = 'TEACHER'
    payment_type: str = 'HOURLY'
    fixed_amount: float
    hour_amount: float
    hour_sup_15_amount: float
    hour_sup_20_amount: float
    hour_sup_30_amount: float
    hour_sup_40_amount: float
    hour_sup_50_amount: float
    day_amount: float
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

__all__ = ["YearlyStaff"]

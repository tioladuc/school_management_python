from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class SubscriptionDto:
    id: int
    company_id: int
    plan_code: str
    start_date: date
    end_date: date
    status: str

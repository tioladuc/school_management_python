from dataclasses import dataclass

@dataclass(frozen=True)
class SubscriptionSuspended:
    entity_id: int
    company_id: int

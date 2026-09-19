from dataclasses import dataclass

@dataclass(frozen=True)
class SubscriptionActivated:
    entity_id: int
    company_id: int

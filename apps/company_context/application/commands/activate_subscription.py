from dataclasses import dataclass

@dataclass(frozen=True)
class ActivateSubscriptionCommand:
    subscription_id: int

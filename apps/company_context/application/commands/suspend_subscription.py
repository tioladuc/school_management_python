from dataclasses import dataclass

@dataclass(frozen=True)
class SuspendSubscriptionCommand:
    subscription_id: int

from typing import Protocol, Any

class EventPublisherPort(Protocol):
    def publish(self, event: Any) -> None: ...

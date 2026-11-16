from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.instalment_base import InstalmentBase


@dataclass(frozen=True)
class InstalmentBaseDto:
    instalment_id: int
    class_room_id: int
    amount: int
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return InstalmentBase(
            instalment_id=m.instalment_id,
            class_room_id=m.class_room_id,
            amount=m.amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return InstalmentBaseDto(
            instalment_id=m.instalment_id,
            class_room_id=m.class_room_id,
            amount=m.amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["InstalmentBaseDto"]

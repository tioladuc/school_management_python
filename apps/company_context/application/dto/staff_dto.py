from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.staff import Staff


@dataclass(frozen=True)
class StaffDto:
    staff_number: str
    first_name: str
    last_name: str
    email: str
    phone: str
    position: str
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return Staff(
            staff_number=m.staff_number,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            position=m.position,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return StaffDto(
            staff_number=m.staff_number,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            position=m.position,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["StaffDto"]

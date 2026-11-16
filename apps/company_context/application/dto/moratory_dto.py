from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.moratory import Moratory


@dataclass(frozen=True)
class MoratoryDto:
    yearly_student_id: int
    start_date: datetime
    end_date: datetime
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return Moratory(
            yearly_student_id=m.yearly_student_id,
            start_date=m.start_date,
            end_date=m.end_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return MoratoryDto(
            yearly_student_id=m.yearly_student_id,
            start_date=m.start_date,
            end_date=m.end_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["MoratoryDto"]

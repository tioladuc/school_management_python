from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.student_move_scan import StudentMoveScan


@dataclass(frozen=True)
class StudentMoveScanDto:
    yearly_student_id: int
    scan_date: datetime
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return StudentMoveScan(
            yearly_student_id=m.yearly_student_id,
            scan_date=m.scan_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return StudentMoveScanDto(
            yearly_student_id=m.yearly_student_id,
            scan_date=m.scan_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["StudentMoveScanDto"]

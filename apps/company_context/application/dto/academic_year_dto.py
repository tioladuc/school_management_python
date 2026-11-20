from dataclasses import dataclass
from datetime import date, datetime

from apps.company_context.domain.entities.academic_year import AcademicYear


@dataclass(frozen=True)
class AcademicYearDto:
    school_id: int
    year: int
    start_date: date
    end_date: date
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return AcademicYear(
            school_id=m.school_id,
            year=m.year,
            start_date=m.start_date,
            end_date=m.end_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return AcademicYearDto(
            school_id=m.school_id,
            year=m.year,
            start_date=m.start_date,
            end_date=m.end_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["AcademicYearDto"]

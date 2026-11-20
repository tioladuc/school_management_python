from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.discipline_year import DisciplineYear


@dataclass(frozen=True)
class DisciplineYearDto:
    yearly_student_id: int
    justified_absence: int
    unjustified_absence: int
    lateness: int
    reserve: int
    notice: int
    blame: int
    exclusion: int
    description: str
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int | None = None
    update_by_id: int | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return DisciplineYear(
            yearly_student_id=m.yearly_student_id,
            justified_absence=m.justified_absence,
            unjustified_absence=m.unjustified_absence,
            lateness=m.lateness,
            reserve=m.reserve,
            notice=m.notice,
            blame=m.blame,
            exclusion=m.exclusion,
            description=m.description,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return DisciplineYearDto(
            yearly_student_id=m.yearly_student_id,
            justified_absence=m.justified_absence,
            unjustified_absence=m.unjustified_absence,
            lateness=m.lateness,
            reserve=m.reserve,
            notice=m.notice,
            blame=m.blame,
            exclusion=m.exclusion,
            description=m.description,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["DisciplineYearDto"]

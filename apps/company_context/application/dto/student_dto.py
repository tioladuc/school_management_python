from dataclasses import dataclass
from datetime import date, datetime

from apps.company_context.domain.entities.student import Student


@dataclass(frozen=True)
class StudentDto:
    code: str
    gov_matricule: str
    first_name: str
    last_name: str
    email: str
    phone: str
    born_at: str
    born_on: date
    gender: str
    password: str
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    id: int | None = None

    @staticmethod
    def to_domain(m):
        return Student(
            code=m.code,
            gov_matricule=m.gov_matricule,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            born_at=m.born_at,
            born_on=m.born_on,
            gender=m.gender,
            password=m.password,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return StudentDto(
            code=m.code,
            gov_matricule=m.gov_matricule,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            born_at=m.born_at,
            born_on=m.born_on,
            gender=m.gender,
            password=m.password,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["StudentDto"]

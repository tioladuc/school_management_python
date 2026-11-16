from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.school import School


@dataclass(frozen=True)
class SchoolDto:
    code: str
    name_fr: str
    name_en: str
    phone: str
    email: str
    address: str
    autorization: str
    founder: str
    principal: str
    city: str
    country: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    id: int | None

    @staticmethod
    def to_domain(m):
        return School(
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            phone=m.phone,
            email=m.email,
            address=m.address,
            autorization=m.autorization,
            founder=m.founder,
            principal=m.principal,
            city=m.city,
            country=m.country,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return SchoolDto(
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            phone=m.phone,
            email=m.email,
            address=m.address,
            autorization=m.autorization,
            founder=m.founder,
            principal=m.principal,
            city=m.city,
            country=m.country,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["SchoolDto"]

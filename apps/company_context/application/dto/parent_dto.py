from dataclasses import dataclass
from datetime import datetime

from apps.company_context.domain.entities.parent import Parent


@dataclass(frozen=True)
class ParentDto:
    code: str
    first_name: str
    last_name: str
    email: str
    phone: str
    profession: str
    gender: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    id: int | None

    @staticmethod
    def to_domain(m):
        return Parent(
            code=m.code,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            profession=m.profession,
            gender=m.gender,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return ParentDto(
            code=m.code,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            profession=m.profession,
            gender=m.gender,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["ParentDto"]

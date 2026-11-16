from dataclasses import dataclass
from datetime import date, datetime

from apps.company_context.domain.entities.booking import Booking


@dataclass(frozen=True)
class BookingDto:
    book_id: int
    yearly_student_id: int
    booking_date: date
    return_date: date
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    created_by_id: int
    update_by_id: int
    id: int | None

    @staticmethod
    def to_domain(m):
        return Booking(
            book_id=m.book_id,
            yearly_student_id=m.yearly_student_id,
            booking_date=m.booking_date,
            return_date=m.return_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return BookingDto(
            book_id=m.book_id,
            yearly_student_id=m.yearly_student_id,
            booking_date=m.booking_date,
            return_date=m.return_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
            id=m.id,
        )

__all__ = ["BookingDto"]

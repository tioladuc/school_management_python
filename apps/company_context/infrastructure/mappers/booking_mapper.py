from ...domain.entities.booking import Booking


class BookingMapper:

    @staticmethod
    def to_domain(m):
        return Booking(
            id=m.id,
            book_id=m.book_id,
            yearly_student_id=m.yearly_student_id,
            booking_date=m.booking_date,
            return_date=m.return_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.booking_model import BookingModel
            m = BookingModel()

        m.book_id = e.book_id
        m.yearly_student_id = e.yearly_student_id
        m.booking_date = e.booking_date
        m.return_date = e.return_date
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

from ...domain.entities.payment import Payment


class PaymentMapper:

    @staticmethod
    def to_domain(m):
        return Payment(
            id=m.id,
            yearly_student_id=m.yearly_student_id,
            staff_id=m.staff_id,
            deposited_by=m.deposited_by,
            amount=m.amount,
            payment_date=m.payment_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.payment_model import PaymentModel
            m = PaymentModel()

        m.yearly_student_id = e.yearly_student_id
        m.staff_id = e.staff_id
        m.deposited_by = e.deposited_by
        m.amount = e.amount
        m.payment_date = e.payment_date
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

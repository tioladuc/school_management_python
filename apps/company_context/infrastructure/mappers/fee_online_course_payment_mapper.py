from ...domain.entities.fee_online_course_payment import FeeOnlineCoursePayment


class FeeOnlineCoursePaymentMapper:

    @staticmethod
    def to_domain(m):
        return FeeOnlineCoursePayment(
            id=m.id,
            fee_online_course_id=m.fee_online_course_id,
            yearly_student_id=m.yearly_student_id,
            paid_by=m.paid_by,
            paid_on=m.paid_on,
            deposited_amount=m.deposited_amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.fee_online_course_payment_model import FeeOnlineCoursePaymentModel
            m = FeeOnlineCoursePaymentModel()

        m.fee_online_course_id = e.fee_online_course_id
        m.yearly_student_id = e.yearly_student_id
        m.paid_by = e.paid_by
        m.paid_on = e.paid_on
        m.deposited_amount = e.deposited_amount
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

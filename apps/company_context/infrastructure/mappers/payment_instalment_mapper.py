from ...domain.entities.payment_instalment import PaymentInstalment


class PaymentInstalmentMapper:

    @staticmethod
    def to_domain(m):
        return PaymentInstalment(
            id=m.id,
            payment_id=m.payment_id,
            base_instalment_id=m.base_instalment_id,
            description=m.description,
            amount=m.amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.payment_instalment_model import PaymentInstalmentModel
            m = PaymentInstalmentModel()

        m.payment_id = e.payment_id
        m.base_instalment_id = e.base_instalment_id
        m.description = e.description
        m.amount = e.amount
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

from ...domain.entities.pay_static_item_data import PayStaticItemData


class PayStaticItemDataMapper:

    @staticmethod
    def to_domain(m):
        return PayStaticItemData(
            id=m.id,
            pay_static_item_id=m.pay_static_item_id,
            yearly_staff_id=m.yearly_staff_id,
            date_payment=m.date_payment,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.pay_static_item_data_model import PayStaticItemData
            m = PayStaticItemData()

        m.pay_static_item_id = e.pay_static_item_id
        m.yearly_staff_id = e.yearly_staff_id
        m.date_payment = e.date_payment
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

from ...domain.entities.pay_recursive_item_data import PayRecursiveItemData


class PayRecursiveItemDataMapper:

    @staticmethod
    def to_domain(m):
        return PayRecursiveItemData(
            id=m.id,
            pay_recursive_item_id=m.pay_recursive_item_id,
            yearly_staff_id=m.yearly_staff_id,
            start_period=m.start_period,
            end_period=m.end_period,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.pay_recursive_item_data_model import PayRecursiveItemData
            m = PayRecursiveItemData()

        m.pay_recursive_item_id = e.pay_recursive_item_id
        m.yearly_staff_id = e.yearly_staff_id
        m.start_period = e.start_period
        m.end_period = e.end_period
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

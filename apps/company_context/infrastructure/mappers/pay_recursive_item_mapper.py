from ...domain.entities.pay_recursive_item import PayRecursiveItem


class PayRecursiveItemMapper:

    @staticmethod
    def to_domain(m):
        return PayRecursiveItem(
            id=m.id,
            pay_category_id=m.pay_category_id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            order=m.order,
            type_choice=m.type_choice,
            calculation_choice=m.calculation_choice,
            value=m.value,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.pay_recursive_item_model import PayRecursiveItem
            m = PayRecursiveItem()

        m.pay_category_id = e.pay_category_id
        m.code = e.code
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.order = e.order
        m.type_choice = e.type_choice
        m.calculation_choice = e.calculation_choice
        m.value = e.value
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

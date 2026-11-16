from ...domain.entities.finance_item import FinanceItem


class FinanceItemMapper:

    @staticmethod
    def to_domain(m):
        return FinanceItem(
            id=m.id,
            finance_subcategory_id=m.finance_subcategory_id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            initial_amount=m.initial_amount,
            current_amount=m.current_amount,
            finance_type=m.finance_type,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.finance_item_model import FinanceItemModel
            m = FinanceItemModel()

        m.finance_subcategory_id = e.finance_subcategory_id
        m.code = e.code
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.initial_amount = e.initial_amount
        m.current_amount = e.current_amount
        m.finance_type = e.finance_type
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

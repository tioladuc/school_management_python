from ...domain.entities.finance_category import FinanceCategory


class FinanceCategoryMapper:

    @staticmethod
    def to_domain(m):
        return FinanceCategory(
            id=m.id,
            academic_year_id=m.academic_year_id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            initial_amount=m.initial_amount,
            current_amount=m.current_amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.finance_category_model import FinanceCategoryModel
            m = FinanceCategoryModel()

        m.academic_year_id = e.academic_year_id
        m.code = e.code
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.initial_amount = e.initial_amount
        m.current_amount = e.current_amount
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

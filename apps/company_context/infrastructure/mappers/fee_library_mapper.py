from ...domain.entities.fee_library import FeeLibrary


class FeeLibraryMapper:

    @staticmethod
    def to_domain(m):
        return FeeLibrary(
            id=m.id,
            fee_category_id=m.fee_category_id,
            academic_year_id=m.academic_year_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
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
            from ...infrastructure.orm.fee_library_model import FeeLibraryModel
            m = FeeLibraryModel()

        m.fee_category_id = e.fee_category_id
        m.academic_year_id = e.academic_year_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.amount = e.amount
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

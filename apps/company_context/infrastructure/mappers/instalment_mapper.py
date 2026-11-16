from ...domain.entities.instalment import Instalment


class InstalmentMapper:

    @staticmethod
    def to_domain(m):
        return Instalment(
            id=m.id,
            academic_year_id=m.academic_year_id,
            order=m.order,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            start_date=m.start_date,
            end_date=m.end_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.instalment_model import InstalmentModel
            m = InstalmentModel()

        m.academic_year_id = e.academic_year_id
        m.order = e.order
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.start_date = e.start_date
        m.end_date = e.end_date
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

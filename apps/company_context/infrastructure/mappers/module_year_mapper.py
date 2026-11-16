from ...domain.entities.module_year import ModuleYear


class ModuleYearMapper:

    @staticmethod
    def to_domain(m):
        return ModuleYear(
            id=m.id,
            subject_id=m.subject_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.module_year_model import ModuleYearModel
            m = ModuleYearModel()

        m.subject_id = e.subject_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

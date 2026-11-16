from ...domain.entities.assessment import Assessment


class AssessmentMapper:

    @staticmethod
    def to_domain(m):
        return Assessment(
            id=m.id,
            sequence_id=m.sequence_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            coeficient=m.coeficient,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.assessment_model import AssessmentModel
            m = AssessmentModel()

        m.sequence_id = e.sequence_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.coeficient = e.coeficient
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

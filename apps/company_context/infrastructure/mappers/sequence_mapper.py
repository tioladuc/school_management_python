from ...domain.entities.sequence import Sequence


class SequenceMapper:

    @staticmethod
    def to_domain(m):
        return Sequence(
            id=m.id,
            term_id=m.term_id,
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
            from ...infrastructure.orm.sequence_model import SequenceModel
            m = SequenceModel()

        m.term_id = e.term_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.coeficient = e.coeficient
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

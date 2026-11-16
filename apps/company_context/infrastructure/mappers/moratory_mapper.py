from ...domain.entities.moratory import Moratory


class MoratoryMapper:

    @staticmethod
    def to_domain(m):
        return Moratory(
            id=m.id,
            yearly_student_id=m.yearly_student_id,
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
            from ...infrastructure.orm.moratory_model import MoratoryModel
            m = MoratoryModel()

        m.yearly_student_id = e.yearly_student_id
        m.start_date = e.start_date
        m.end_date = e.end_date
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

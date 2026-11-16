from ...domain.entities.discipline_sequence import DisciplineSequence


class DisciplineSequenceMapper:

    @staticmethod
    def to_domain(m):
        return DisciplineSequence(
            id=m.id,
            yearly_student_id=m.yearly_student_id,
            sequence_id=m.sequence_id,
            justified_absence=m.justified_absence,
            unjustified_absence=m.unjustified_absence,
            lateness=m.lateness,
            reserve=m.reserve,
            notice=m.notice,
            blame=m.blame,
            exclusion=m.exclusion,
            description=m.description,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.discipline_sequence_model import DisciplineSequenceModel
            m = DisciplineSequenceModel()

        m.yearly_student_id = e.yearly_student_id
        m.sequence_id = e.sequence_id
        m.justified_absence = e.justified_absence
        m.unjustified_absence = e.unjustified_absence
        m.lateness = e.lateness
        m.reserve = e.reserve
        m.notice = e.notice
        m.blame = e.blame
        m.exclusion = e.exclusion
        m.description = e.description
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

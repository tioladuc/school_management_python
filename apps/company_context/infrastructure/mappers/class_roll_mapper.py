from ...domain.entities.class_roll import ClassRoll


class ClassRollMapper:

    @staticmethod
    def to_domain(m):
        return ClassRoll(
            id=m.id,
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            start_period=m.start_period,
            end_period=m.end_period,
            duration=m.duration,
            teacher_id=m.teacher_id,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.class_roll_model import ClassRollModel
            m = ClassRollModel()

        m.yearly_student_id = e.yearly_student_id
        m.subject_id = e.subject_id
        m.start_period = e.start_period
        m.end_period = e.end_period
        m.duration = e.duration
        m.teacher_id = e.teacher_id
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

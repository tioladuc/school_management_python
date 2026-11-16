from ...domain.entities.student_message import StudentMessage


class StudentMessageMapper:

    @staticmethod
    def to_domain(m):
        return StudentMessage(
            id=m.id,
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            start_period=m.start_period,
            end_period=m.end_period,
            subject_fr=m.subject_fr,
            subject_en=m.subject_en,
            content_fr=m.content_fr,
            content_en=m.content_en,
            teacher_id=m.teacher_id,
            category=m.category,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.student_message_model import StudentMessageModel
            m = StudentMessageModel()

        m.yearly_student_id = e.yearly_student_id
        m.subject_id = e.subject_id
        m.start_period = e.start_period
        m.end_period = e.end_period
        m.subject_fr = e.subject_fr
        m.subject_en = e.subject_en
        m.content_fr = e.content_fr
        m.content_en = e.content_en
        m.teacher_id = e.teacher_id
        m.category = e.category
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

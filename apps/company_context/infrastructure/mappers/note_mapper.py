from ...domain.entities.note import Note


class NoteMapper:

    @staticmethod
    def to_domain(m):
        return Note(
            id=m.id,
            yearly_student_id=m.yearly_student_id,
            subject_id=m.subject_id,
            assessment_id=m.assessment_id,
            mark=m.mark,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.note_model import NoteModel
            m = NoteModel()

        m.yearly_student_id = e.yearly_student_id
        m.subject_id = e.subject_id
        m.assessment_id = e.assessment_id
        m.mark = e.mark
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

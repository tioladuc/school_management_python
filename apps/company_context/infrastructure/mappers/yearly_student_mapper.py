from ...domain.entities.yearly_student import YearlyStudent


class YearlyStudentMapper:

    @staticmethod
    def to_domain(m):
        return YearlyStudent(
            id=m.id,
            student_id=m.student_id,
            academic_year_id=m.academic_year_id,
            class_room_id=m.class_room_id,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.yearly_student_model import YearlyStudentModel
            m = YearlyStudentModel()

        m.student_id = e.student_id
        m.academic_year_id = e.academic_year_id
        m.class_room_id = e.class_room_id
        m.status = e.status

        return m

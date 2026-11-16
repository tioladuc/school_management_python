from ...domain.entities.online_course_reading import OnlineCourseReading


class OnlineCourseReadingMapper:

    @staticmethod
    def to_domain(m):
        return OnlineCourseReading(
            id=m.id,
            online_course_id=m.online_course_id,
            yearly_student_id=m.yearly_student_id,
            reading_date=m.reading_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.online_course_reading_model import OnlineCourseReadingModel
            m = OnlineCourseReadingModel()

        m.online_course_id = e.online_course_id
        m.yearly_student_id = e.yearly_student_id
        m.reading_date = e.reading_date
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

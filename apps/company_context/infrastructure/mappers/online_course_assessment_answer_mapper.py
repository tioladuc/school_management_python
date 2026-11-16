from ...domain.entities.online_course_assessment_answer import OnlineCourseAssessmentAnswer


class OnlineCourseAssessmentAnswerMapper:

    @staticmethod
    def to_domain(m):
        return OnlineCourseAssessmentAnswer(
            id=m.id,
            online_course_assessment_id=m.online_course_assessment_id,
            yearly_staff_id=m.yearly_staff_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            file_path=m.file_path,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.online_course_assessment_answer_model import OnlineCourseAssessmentAnswerModel
            m = OnlineCourseAssessmentAnswerModel()

        m.online_course_assessment_id = e.online_course_assessment_id
        m.yearly_staff_id = e.yearly_staff_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.file_path = e.file_path
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

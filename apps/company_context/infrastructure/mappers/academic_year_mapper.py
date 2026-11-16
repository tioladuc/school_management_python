from ...domain.entities.academic_year import AcademicYear


class AcademicYearMapper:

    @staticmethod
    def to_domain(m):
        return AcademicYear(
            id=m.id,
            school_id=m.school_id,
            year=m.year,
            start_date=m.start_date,
            end_date=m.end_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.academic_year_model import AcademicYearModel
            m = AcademicYearModel()

        m.school_id = e.school_id
        m.year = e.year
        m.start_date = e.start_date
        m.end_date = e.end_date
        m.status = e.status

        return m

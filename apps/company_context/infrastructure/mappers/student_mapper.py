from ...domain.entities.student import Student


class StudentMapper:

    @staticmethod
    def to_domain(m):
        return Student(
            id=m.id,
            code=m.code,
            gov_matricule=m.gov_matricule,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            born_at=m.born_at,
            born_on=m.born_on,
            gender=m.gender,
            password = m.password,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ..orm.student_model import StudentModule
            m = StudentModule()

        m.code = e.code
        m.gov_matricule = e.gov_matricule
        m.first_name = e.first_name
        m.last_name = e.last_name
        m.email = e.email
        m.phone = e.phone
        m.born_at = e.born_at
        m.born_on = e.born_on
        m.gender = e.gender
        m.password = e.password,
        m.status = e.status

        return m

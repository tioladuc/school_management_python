from ...domain.entities.parent import Parent


class ParentMapper:

    @staticmethod
    def to_domain(m):
        return Parent(
            id=m.id,
            code=m.code,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            profession=m.profession,
            gender=m.gender,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.parent_model import ParentModule
            m = ParentModule()

        m.code = e.code
        m.first_name = e.first_name
        m.last_name = e.last_name
        m.email = e.email
        m.phone = e.phone
        m.profession = e.profession
        m.gender = e.gender
        m.status = e.status

        return m


from ...domain.entities.school import School


class SchoolMapper:

    @staticmethod
    def to_domain(m):
        return School(
            id=m.id,
            code=m.code,
            name_fr=m.name_fr,
            name_en=m.name_en,
            phone=m.phone,
            email=m.email,
            address=m.address,
            autorization=m.autorization,
            founder=m.founder,
            principal=m.principal,
            city=m.city,
            country=m.country,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.school_model import SchoolModel
            m = SchoolModel()

        m.code = e.code
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.phone = e.phone
        m.email = e.email
        m.address = e.address
        m.autorization = e.autorization
        m.founder = e.founder
        m.principal = e.principal
        m.city = e.city
        m.country = e.country
        m.status = e.status

        return m

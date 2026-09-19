from ...domain.entities.school import School
class SchoolMapper:
    @staticmethod
    def to_domain(m): return School(m.id,m.company_id,m.code,m.name,m.city,m.country,m.status,m.created_at,m.updated_at)
    @staticmethod
    def to_model(e,m): m.company_id=e.company_id;m.code=e.code;m.name=e.name;m.city=e.city;m.country=e.country;m.status=e.status;return m

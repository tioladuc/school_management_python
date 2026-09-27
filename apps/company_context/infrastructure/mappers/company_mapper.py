from ...domain.entities.company import Company
from ...domain.value_objects.company_code import CompanyCode


class CompanyMapper:
    @staticmethod
    def to_domain(m):
        print(f"Mapping model to domain: {m}")
        return Company(
            m.id, #m["id"],
            CompanyCode(m.code),#CompanyCode(m["code"]),
            m.name,#m["name"],
            m.email,#m["email"],
            m.phone,#m["phone"],
            m.address,#m["address"],
            m.status,#m["status"],
            m.created_at, #None, # m["created_at"],
            m.updated_at, #None, # m["updated_at"],
        )

    @staticmethod
    def to_model(e, m):
        m.code = e.code.value
        m.name = e.name
        m.email = e.email
        m.phone = e.phone
        m.address = e.address
        m.status = e.status
        return m

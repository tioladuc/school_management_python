from ...domain.entities.staff import Staff
class StaffMapper:
    @staticmethod
    def to_domain(m): return Staff(m.id,m.company_id,m.staff_number,m.first_name,m.last_name,m.email,m.phone,m.position,m.status,m.created_at,m.updated_at)
    @staticmethod
    def to_model(e,m): m.company_id=e.company_id;m.staff_number=e.staff_number;m.first_name=e.first_name;m.last_name=e.last_name;m.email=e.email;m.phone=e.phone;m.position=e.position;m.status=e.status;return m

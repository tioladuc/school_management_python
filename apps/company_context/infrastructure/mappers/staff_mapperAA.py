from ...domain.entities.staff import Staff


class StaffMapper:

    @staticmethod
    def to_domain(m):
        return Staff(
            id=m.id,
            staff_number=m.staff_number,
            first_name=m.first_name,
            last_name=m.last_name,
            email=m.email,
            phone=m.phone,
            position=m.position,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.staff_model import StaffModel
            m = StaffModel()

        m.staff_number = e.staff_number
        m.first_name = e.first_name
        m.last_name = e.last_name
        m.email = e.email
        m.phone = e.phone
        m.position = e.position
        m.status = e.status

        return m

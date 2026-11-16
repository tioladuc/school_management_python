from ...domain.entities.student_parent import StudentParent


class StudentParentMapper:

    @staticmethod
    def to_domain(m):
        return StudentParent(
            id=m.id,
            student_id=m.student_id,
            parent_id=m.parent_id,
            relation=m.relation,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.student_parent_module import StudentParentModule
            m = StudentParentModule()

        m.student_id = e.student_id
        m.parent_id = e.parent_id
        m.relation = e.relation
        m.status = e.status

        return m

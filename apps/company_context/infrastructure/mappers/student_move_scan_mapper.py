from ...domain.entities.student_move_scan import StudentMoveScan


class StudentMoveScanMapper:

    @staticmethod
    def to_domain(m):
        return StudentMoveScan(
            id=m.id,
            yearly_student_id=m.yearly_student_id,
            scan_date=m.scan_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.student_move_scan_model import StudentMoveScanModel
            m = StudentMoveScanModel()

        m.yearly_student_id = e.yearly_student_id
        m.scan_date = e.scan_date
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m

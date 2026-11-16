from ...domain.entities.yearly_staff import YearlyStaff


class YearlyStaffMapper:

    @staticmethod
    def to_domain(m):
        return YearlyStaff(
            id=m.id,
            academic_year_id=m.academic_year_id,
            staff_id=m.staff_id,
            profile=m.profile,
            payment_type=m.payment_type,
            fixed_amount=m.fixed_amount,
            hour_amount=m.hour_amount,
            hour_sup_15_amount=m.hour_sup_15_amount,
            hour_sup_20_amount=m.hour_sup_20_amount,
            hour_sup_30_amount=m.hour_sup_30_amount,
            hour_sup_40_amount=m.hour_sup_40_amount,
            hour_sup_50_amount=m.hour_sup_50_amount,
            day_amount=m.day_amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.yearly_staff_model import YearlyStaffModel
            m = YearlyStaffModel()

        m.academic_year_id = e.academic_year_id
        m.staff_id = e.staff_id
        m.profile = e.profile
        m.payment_type = e.payment_type
        m.fixed_amount = e.fixed_amount
        m.hour_amount = e.hour_amount
        m.hour_sup_15_amount = e.hour_sup_15_amount
        m.hour_sup_20_amount = e.hour_sup_20_amount
        m.hour_sup_30_amount = e.hour_sup_30_amount
        m.hour_sup_40_amount = e.hour_sup_40_amount
        m.hour_sup_50_amount = e.hour_sup_50_amount
        m.day_amount = e.day_amount
        m.status = e.status

        return m

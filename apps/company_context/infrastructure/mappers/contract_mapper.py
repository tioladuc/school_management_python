from ...domain.entities.contract import Contract
class ContractMapper:
    @staticmethod
    def to_domain(m): return Contract(m.id,m.company_id,m.signature_date,m.company_setup_price,m.school_setup_price,m.academic_year_renewal_price,m.start_date,m.end_date,m.status,m.currency)
    @staticmethod
    def to_model(e,m): m.company_id=e.company_id;m.signature_date=e.signature_date;m.company_setup_price=e.company_setup_price;m.school_setup_price=e.school_setup_price;m.academic_year_renewal_price=e.academic_year_renewal_price;m.start_date=e.start_date;m.end_date=e.end_date;m.status=e.status;m.currency=e.currency;return m

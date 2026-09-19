from ...domain.entities.contract_data import ContractData
class ContractDataMapper:
    @staticmethod
    def to_domain(m): return ContractData(m.id,m.contract_id,m.transaction_type,m.transaction_date,m.quantity,m.unit_price,m.total_amount,m.description)
    @staticmethod
    def to_model(e,m): m.contract_id=e.contract_id;m.transaction_type=e.transaction_type;m.transaction_date=e.transaction_date;m.quantity=e.quantity;m.unit_price=e.unit_price;m.total_amount=e.total_amount;m.description=e.description;return m

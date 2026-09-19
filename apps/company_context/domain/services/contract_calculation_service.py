from decimal import Decimal
from ..entities.contract_data import ContractData
from datetime import date

class ContractCalculationService:
    def calculate(self, contract, transaction_type, quantity, unit_price, description=''):
        quantity = Decimal(quantity)
        unit_price = Decimal(unit_price)
        return ContractData(
            id=None, contract_id=contract.id, transaction_type=transaction_type,
            transaction_date=date.today(), quantity=quantity, unit_price=unit_price,
            total_amount=quantity * unit_price, description=description,
        )

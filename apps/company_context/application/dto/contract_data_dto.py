from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

from apps.company_context.domain.entities.contract_data import ContractData


@dataclass(frozen=True)
class ContractDataDto:
    contract_id: int
    transaction_type: str
    transaction_date: date
    quantity: Decimal
    unit_price: Decimal
    total_amount: Decimal
    description: str
    status: str
    created_at: datetime | None
    updated_at: datetime | None
    id: int | None

    @staticmethod
    def to_domain(m):
        return ContractData(
            contract_id=m.contract_id,
            transaction_type=m.transaction_type,
            transaction_date=m.transaction_date,
            quantity=m.quantity,
            unit_price=m.unit_price,
            total_amount=m.total_amount,
            description=m.description,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

    @staticmethod
    def to_dto(m):
        return ContractDataDto(
            contract_id=m.contract_id,
            transaction_type=m.transaction_type,
            transaction_date=m.transaction_date,
            quantity=m.quantity,
            unit_price=m.unit_price,
            total_amount=m.total_amount,
            description=m.description,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            id=m.id,
        )

__all__ = ["ContractDataDto"]

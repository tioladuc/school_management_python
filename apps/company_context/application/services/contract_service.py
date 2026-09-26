from ...domain.entities.contract import Contract
from ...domain.services.contract_activation_service import ContractActivationService
from ...domain.exceptions import NotFoundError
from ..dto.contract_dto import ContractDto


class ContractApplicationService:
    def __init__(self, contracts):
        self.contracts = contracts

    def create(self, command):
        entity = Contract(
            None,
            command.company_id,
            command.signature_date,
            command.company_setup_price,
            command.school_setup_price,
            command.academic_year_renewal_price,
            command.start_date,
            command.end_date,
            "DRAFT",
            command.currency,
        )
        return self.to_dto(self.contracts.save(entity))

    def update(self, command):
        c = self.contracts.get(command.contract_id)
        if c is None:
            raise NotFoundError("Contract not found.")
        (
            c.signature_date,
            c.company_setup_price,
            c.school_setup_price,
            c.academic_year_renewal_price,
            c.start_date,
            c.end_date,
        ) = (
            command.signature_date,
            command.company_setup_price,
            command.school_setup_price,
            command.academic_year_renewal_price,
            command.start_date,
            command.end_date,
        )
        return self.to_dto(self.contracts.save(c))

    def activate(self, command):
        c = self.contracts.get(command.contract_id)
        if c is None:
            raise NotFoundError("Contract not found.")
        return self.to_dto(self.contracts.save(ContractActivationService().activate(c)))

    def suspend(self, command):
        c = self.contracts.get(command.contract_id)
        if c is None:
            raise NotFoundError("Contract not found.")
        c.suspend()
        return self.to_dto(self.contracts.save(c))

    def renew(self, command):
        c = self.contracts.get(command.contract_id)
        if c is None:
            raise NotFoundError("Contract not found.")
        if command.new_end_date <= c.end_date:
            raise ValueError(
                "New contract end date must be later than the current end date."
            )
        c.end_date = command.new_end_date
        c.status = "ACTIVE"
        return self.to_dto(self.contracts.save(c))

    def get(self, query):
        c = self.contracts.get(query.contract_id)
        if c is None:
            raise NotFoundError("Contract not found.")
        return self.to_dto(c)

    def active(self, query):
        c = self.contracts.get_active_for_company(query.company_id)
        return self.to_dto(c) if c else None

    @staticmethod
    def to_dto(c):
        return ContractDto(
            c.id,
            c.company_id,
            c.signature_date,
            c.company_setup_price,
            c.school_setup_price,
            c.academic_year_renewal_price,
            c.start_date,
            c.end_date,
            c.status,
            c.currency,
        )

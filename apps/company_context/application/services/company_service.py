from ...domain.entities.company import Company
from ...domain.value_objects.company_code import CompanyCode
from ...domain.services.company_domain_service import CompanyDomainService
from ...domain.services.company_activation_service import CompanyActivationService
from ...domain.services.company_suspension_service import CompanySuspensionService
from ...domain.exceptions import ConflictError, NotFoundError
from ..dto.company_dto import CompanyDto

class CompanyApplicationService:
    def __init__(self, companies, events=None):
        self.companies = companies
        self.events = events

    def create(self, command):
        if self.companies.exists_by_code(command.code):
            raise ConflictError('Company code already exists.')
        company = Company(None, CompanyCode(command.code), command.name.strip(), command.email.strip(), command.phone.strip(), command.address.strip())
        company = self.companies.save(company)
        return self.to_dto(company)

    def update(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        CompanyDomainService.ensure_active(company)
        company.name, company.email, company.phone, company.address = command.name.strip(), command.email.strip(), command.phone.strip(), command.address.strip()
        return self.to_dto(self.companies.save(company))

    def activate(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        return self.to_dto(self.companies.save(CompanyActivationService().activate(company)))

    def suspend(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        return self.to_dto(self.companies.save(CompanySuspensionService().suspend(company)))

    def get(self, query):
        company = self.companies.get(query.company_id)
        if company is None: raise NotFoundError('Company not found.')
        return self.to_dto(company)

    def search(self, query):
        return [self.to_dto(c) for c in self.companies.search(query.search, query.status)]

    @staticmethod
    def to_dto(c):
        return CompanyDto(c.id, c.code.value, c.name, c.email, c.phone, c.address, c.status)

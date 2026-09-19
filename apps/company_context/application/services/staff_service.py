from ...domain.entities.staff import Staff
from ...domain.services.staff_domain_service import StaffDomainService
from ...domain.exceptions import ConflictError, NotFoundError
from ..dto.staff_dto import StaffDto

class StaffApplicationService:
    def __init__(self, staff, companies): self.staff, self.companies = staff, companies
    def create(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        StaffDomainService().ensure_staff_creation_allowed(company)
        if self.staff.exists_by_number(command.company_id, command.staff_number): raise ConflictError('Staff number already exists.')
        entity = Staff(None, command.company_id, command.staff_number.strip(), command.first_name.strip(), command.last_name.strip(), command.email.strip(), command.phone.strip(), command.position.strip())
        return self.to_dto(self.staff.save(entity))
    def update(self, command):
        entity = self.staff.get(command.staff_id)
        if entity is None: raise NotFoundError('Staff not found.')
        entity.first_name, entity.last_name, entity.email, entity.phone, entity.position = command.first_name.strip(), command.last_name.strip(), command.email.strip(), command.phone.strip(), command.position.strip()
        return self.to_dto(self.staff.save(entity))
    def get(self, query):
        entity = self.staff.get(query.staff_id)
        if entity is None: raise NotFoundError('Staff not found.')
        return self.to_dto(entity)
    def search(self, query): return [self.to_dto(s) for s in self.staff.search(query.company_id, query.search)]
    @staticmethod
    def to_dto(s): return StaffDto(s.id, s.company_id, s.staff_number, s.first_name, s.last_name, s.email, s.phone, s.position, s.status)

from apps.company_context.infrastructure.repositories.school_repository import SchoolRepository

from ...domain.entities.school import School
from ...domain.services.school_registration_service import SchoolRegistrationService
from ...domain.exceptions import ConflictError, NotFoundError
from ..dto.school_dto import SchoolDto


class SchoolApplicationServiceBK:
    def __init__(self, schools, companies, contracts, events=None):
        self.schools, self.companies, self.contracts, self.events = schools, companies, contracts, events

    def create(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        contract = self.contracts.get_active_for_company(command.company_id)
        if self.schools.exists_by_code(command.company_id, command.code): raise ConflictError('School code already exists within the company.')
        school = School(None, command.company_id, command.code.strip().upper(), command.name.strip(), command.city.strip(), command.country.strip())
        school = SchoolRegistrationService().register(company, school, contract)
        school = self.schools.save(school)
        if self.events: self.events.publish(('SchoolCreated', school.id, school.company_id))
        return self.to_dto(school)

    def update(self, command):
        school = self.schools.get(command.school_id)
        if school is None: raise NotFoundError('School not found.')
        school.name, school.city, school.country = command.name.strip(), command.city.strip(), command.country.strip()
        return self.to_dto(self.schools.save(school))

    def get(self, query):
        school = self.schools.get(query.school_id)
        if school is None: raise NotFoundError('School not found.')
        return self.to_dto(school)

    def list(self, query):
        return [self.to_dto(s) for s in self.schools.list_by_company(query.company_id)]

    @staticmethod
    def to_dto(s): return SchoolDto(s.id, s.company_id, s.code, s.name, s.city, s.country, s.status)

# ===========================================================================
class SchoolApplicationService:
    def __init__(self, schools, events=None):
        self.events = events
        self.repository = schools #SchoolRepository()

    def get_all(self, db_alias="default"):
        #return self.repository.get_all(db_alias)
        return [self.to_dto(s) for s in self.repository.get_all(db_alias)]

    def get_by_id(self, academic_year_id, db_alias="default"):
        return self.to_dto(self.repository.get_by_id(academic_year_id, db_alias))        
    
    def create(self, data, db_alias="default"):
        return self.to_dto(self.repository.create(data, db_alias))
        # return SchoolModel.objects.using(db_alias).create(**data)
    
    def update(self, academic_year_id, data, db_alias="default"):
        return self.to_dto(self.repository.update(academic_year_id, data, db_alias))
    #        return SchoolModel.objects.using(db_alias).filter(
    #            id=academic_year_id
    #        ).update(**data)
    
    def delete(self, academic_year_id, db_alias="default"):
        return self.repository.delete(academic_year_id, db_alias)
    #       return SchoolModel.objects.using(db_alias).filter(
    #            id=academic_year_id
    #        ).delete()
    







    def create(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        contract = self.contracts.get_active_for_company(command.company_id)
        if self.schools.exists_by_code(command.company_id, command.code): raise ConflictError('School code already exists within the company.')
        school = School(None, command.company_id, command.code.strip().upper(), command.name.strip(), command.city.strip(), command.country.strip())
        school = SchoolRegistrationService().register(company, school, contract)
        school = self.schools.save(school)
        if self.events: self.events.publish(('SchoolCreated', school.id, school.company_id))
        return self.to_dto(school)

    def update(self, command):
        school = self.schools.get(command.school_id)
        if school is None: raise NotFoundError('School not found.')
        school.name, school.city, school.country = command.name.strip(), command.city.strip(), command.country.strip()
        return self.to_dto(self.schools.save(school))

    def get(self, query):
        school = self.schools.get(query.school_id)
        if school is None: raise NotFoundError('School not found.')
        return self.to_dto(school)

    def list(self, query):
        return [self.to_dto(s) for s in self.schools.list_by_company(query.company_id)]

    @staticmethod
    def to_dto(s): return SchoolDto(s.id, s.company_id, s.code, s.name, s.city, s.country, s.status)

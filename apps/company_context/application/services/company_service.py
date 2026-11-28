from apps.company_context.application.dto.parent_dto import ParentDto
from apps.company_context.application.services.school_service import SchoolApplicationService

from ...domain.entities.company import Company
from ...domain.value_objects.company_code import CompanyCode
from ...domain.services.company_domain_service import CompanyDomainService
from ...domain.services.company_activation_service import CompanyActivationService
from ...domain.services.company_suspension_service import CompanySuspensionService
from ...domain.exceptions import ConflictError, NotFoundError
from ..dto.company_dto import CompanyDto
from types import SimpleNamespace

class CompanyApplicationService:
    STAFF = 'STAFF'
    STUDENT = 'STUDENT'
    PARENT = 'PARENT'
    SUPERADMIN = 'SUPERADMIN'

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
        company.name, company.email, company.phone, company.address, company.tenant_database = command.name.strip(), command.email.strip(), command.phone.strip(), command.address.strip(), command.tenant_database.strip()
        return self.to_dto(self.companies.save(company))

    def activate(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        return self.to_dto(self.companies.save(CompanyActivationService().activate(company)))

    def suspend(self, command):
        company = self.companies.get(command.company_id)
        if company is None: raise NotFoundError('Company not found.')
        return self.to_dto(self.companies.save(CompanySuspensionService().suspend(company)))

    def delete(self, command):
            print('FFFFFFFFFFFFFFFFFFFFFFFFFFFF', command.company_id)
            #print('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
            #company = self.companies.get(command.company_id)
            #print('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD UUUUUUUUUUUUUU')
            #if company is None: raise NotFoundError('Company not found.')
            return self.companies.delete(command.company_id)

    def get(self, query):
        company = self.companies.get(query.company_id)
        if company is None: raise NotFoundError('Company not found.')
        return self.to_dto(company)

    def search(self, query):
        return [self.to_dto(c) for c in self.companies.search(query.search, query.status)]
    
    def getProfiles(self):
        return [
            {'value': self.STAFF, 'label': 'Staff / Personnel'},
            {'value': self.STUDENT, 'label': 'Student / Eleve'},
            {'value': self.PARENT, 'label': 'Parent'},
            {'value': self.SUPERADMIN, 'label': 'Super-Administrator'}
        ]
    def getStaffProfiles(self):
        return [
            {'value': 'TEACHER', 'label': 'Teacher'},
            {'value': 'ACCOUNTANT', 'label': 'Accountant'},
            {'value': 'HEADMASTER', 'label': 'Head Master'},
            {'value': 'ASSISTANT', 'label': 'Administrative Assistant'}
        ]

    """def getSchools(self):
        return [
            {"value": "SCH_FDL_001", "label": "Collège François-de-Laval"},
            {"value": "SCH_STP_002", "label": "St-Patrick's High School"},
            {"value": "SCH_URS_003", "label": "École des Ursulines de Québec"},
            {"value": "SCH_STR_004", "label": "École Secondaire Saint-Roch"},
            {"value": "SCH_GAR_005", "label": "Collège Garneau"}
        ]"""

    def login(self, userInDto):
        print(userInDto.company_code , "========666666666666666")
        company = self.companies.get_by_code(userInDto.company_code)
        print(company)
        if company is None:
            return {"success": False, "message": "Company not found."}
        if company.status != "ACTIVE":
            return {"success": False, "message": "Company is not active."}
        # Here you would typically check the user's credentials against a user repository
        # For this example, we'll assume the login is successful if the company is active
        data = {"success": True, "message": "Login successful.", "user_data": None, "alias": company.alias}
        return SimpleNamespace(**data)
        return {"success": True, "message": "Login successful.", "user_data": None}

    def loginBeta(self, request, alias, school_id, profile_key, login, password):
        resultProfile = next((item for item in self.getProfiles() if item["value"] == profile_key), None)

        if resultProfile is None:
            return False
        
        if resultProfile['value'] == self.PARENT:
            return self._loginParent(request, alias, school_id, resultProfile, login, password)
        
        if resultProfile['value'] == self.STAFF:
            return self._loginStaff(request, alias, school_id, resultProfile, login, password)
        
        if resultProfile['value'] == self.STUDENT:
            return self._loginStudent(request, alias, school_id, resultProfile, login, password)
        
        if resultProfile['value'] == self.SUPERADMIN:
            return self._loginSuperadmin(request, alias, school_id, resultProfile, login, password)
                
        return True

    def _loginParent(self, request, alias, school_id, resultProfile, login, password):
        service = SchoolApplicationService()
        service.get_all(ParentDto, alias)

        return True    

    def _loginStaff(self, request, alias, school_id, resultProfile, login, password):
        return True

    def _loginStudent(self, request, alias, school_id, resultProfile, login, password):
        return True

    def _loginSuperadmin(self, request, alias, school_id, resultProfile, login, password):
        return True

    # For company database initialization and school creation
    def initialize_company_bd_with_empty_basic_tables(self, company_id):
        try:
            self.companies.initialize_company_bd_with_empty_basic_tables(company_id)
            return True
        except :
            return False
    
    def prepare_empty_tables_for_school(self, company_id):
        try:
            self.companies.prepare_empty_tables_for_school(company_id)
            return True
        except :
            return False 

    def prepare_sample_data_for_school(self, company_id):
        try:
            self.companies.prepare_sample_data_for_school(company_id)
            return True
        except :
            return False 
    
    def drop_database(self, company_id):
        try:
            self.companies.drop_database(company_id)
            return True
        except :
            return False 
    
    def backup_company_database(self, company_id):
        try:
            self.companies.backup_company_database(company_id)
            return True
        except :
            return False 







    

    def create_school_from_scratch(self, company_id):
        try:
            self.companies.create_school_from_scratch(company_id)
            return True
        except :
            return False
    
    def create_school_from_school(self, company_id, school_code):
        try:
            self.companies.create_school_from_school(company_id, school_code)
            return True
        except :
            return False 

    


    
    @staticmethod
    def to_dto(c):
        return CompanyDto(c.id, c.code.value, c.name, c.email, c.phone, c.address, c.status, c.tenant_database, c.alias)

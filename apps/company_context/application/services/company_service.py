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

    def get(self, query):
        company = self.companies.get(query.company_id)
        if company is None: raise NotFoundError('Company not found.')
        return self.to_dto(company)

    def search(self, query):
        return [self.to_dto(c) for c in self.companies.search(query.search, query.status)]
    
    def getProfiles(self):
        return [
            {'value': 'SUPER_ADMINISTRATOR', 'label': 'Super Administrator'},
            {'value': 'ADMINISTRATOR', 'label': 'Administrator'},
            {'value': 'ADMINISTRATION', 'label': 'Administration'},
            {'value': 'STUDENT', 'label': 'Student'},
            {'value': 'PARENT', 'label': 'Parent'},
            {'value': 'TEACHER', 'label': 'Teacher'},
            {'value': 'ACCOUNTANT', 'label': 'Accountant'}
        ]

    def getSchools(self):
        return [
            {"value": "SCH_FDL_001", "label": "Collège François-de-Laval"},
            {"value": "SCH_STP_002", "label": "St-Patrick's High School"},
            {"value": "SCH_URS_003", "label": "École des Ursulines de Québec"},
            {"value": "SCH_STR_004", "label": "École Secondaire Saint-Roch"},
            {"value": "SCH_GAR_005", "label": "Collège Garneau"}
        ]

    def login(self, userInDto):
        company = self.companies.get_by_code(userInDto.company_code)
        if company is None:
            return {"success": False, "message": "Company not found."}
        if company.status != "ACTIVE":
            return {"success": False, "message": "Company is not active."}
        # Here you would typically check the user's credentials against a user repository
        # For this example, we'll assume the login is successful if the company is active
        return {"success": True, "message": "Login successful.", "user_data": None}


    # For company database initialization and school creation
    def initialize_company_bd(self, company_id):
        try:
            self.companies.initialize_company_bd(company_id)
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

    def preparer_tables_for_school(self, company_id):
            try:
                self.companies.preparer_tables_for_school(company_id)
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



    
    @staticmethod
    def to_dto(c):
        return CompanyDto(c.id, c.code.value, c.name, c.email, c.phone, c.address, c.status, c.tenant_database)

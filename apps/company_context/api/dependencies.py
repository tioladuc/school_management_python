from ..infrastructure.repositories.company_repository import CompanyRepository
from ..infrastructure.repositories.school_repository import SchoolRepository
from ..infrastructure.repositories.staff_repository import StaffRepository
from ..infrastructure.repositories.contract_repository import ContractRepository
from ..infrastructure.repositories.contract_data_repository import ContractDataRepository
from ..infrastructure.events.in_memory_publisher import InMemoryEventPublisher
from ..application.services.company_service import CompanyApplicationService
from ..application.services.school_service import SchoolApplicationService
from ..application.services.staff_service import StaffApplicationService
from ..application.services.contract_service import ContractApplicationService
from ..application.services.contract_billing_service import ContractBillingApplicationService

_events=InMemoryEventPublisher()

def services():
    companies=CompanyRepository();schools=SchoolRepository();staff=StaffRepository();contracts=ContractRepository();data=ContractDataRepository()
    return {
      'company':CompanyApplicationService(companies,_events),
      'school':SchoolApplicationService(schools,companies,contracts,_events),
      'staff':StaffApplicationService(staff,companies),
      'contract':ContractApplicationService(contracts),
      'billing':ContractBillingApplicationService(contracts,data),
    }

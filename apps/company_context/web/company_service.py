from urllib import request

from apps.company_context.application.services.company_service import (
    CompanyApplicationService,
)

from apps.company_context.application.services.school_service import SchoolApplicationService
from apps.company_context.infrastructure.repositories.company_repository import (
    CompanyRepository,
)
from apps.company_context.infrastructure.repositories.school_repository import SchoolRepository


def get_company_service():
    repository = CompanyRepository()

    return CompanyApplicationService(
        companies=repository,
    )

def get_school_service(alias):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", alias)
    repository = SchoolRepository(connection_alias=alias)
    return SchoolApplicationService(
        schools=repository
    )
from apps.company_context.application.services.company_service import (
    CompanyApplicationService,
)

from apps.company_context.infrastructure.repositories.company_repository import (
    CompanyRepository,
)


def get_company_service():
    repository = CompanyRepository()

    return CompanyApplicationService(
        companies=repository,
    )
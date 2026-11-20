from urllib import request

from django.db import connections

from apps.company_context.application.services.company_service import (
    CompanyApplicationService,
)

from apps.company_context.application.services.school_serviceAAA import (
    SchoolApplicationServiceAAA,
)

from apps.company_context.application.services.school_service import SchoolApplicationService
from apps.company_context.infrastructure.repositories.company_repository import (
    CompanyRepository,
)
from apps.company_context.infrastructure.repositories.school_repository import SchoolRepository
from config import settings
from config.startup import parse_connection_string


def get_company_service():
    repository = CompanyRepository()

    return CompanyApplicationService(
        companies=repository,
    )

def get_school_service(alias):
    repository = SchoolRepository(connection_alias=alias)
    return SchoolApplicationService(
        schools=repository
    )

def get_school_serviceAAA():
    return SchoolApplicationServiceAAA()

def update_company_tenant_database(alias, tenant_database, request, delete_alias=False):
    if delete_alias == False:
        database_config = parse_connection_string(tenant_database)            
        # Register with Django's connection handler.
        settings.DATABASES[alias] = database_config
        connections.databases[alias] = database_config
        request.session["alias"] = alias

    else:
        if alias in settings.DATABASES and alias != 'default':

            connections[alias].close()
            settings.DATABASES.pop(alias, None)
            connections.databases.pop(alias, None)
            request.session["alias"] = "default"
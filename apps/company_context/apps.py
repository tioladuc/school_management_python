from django.apps import AppConfig
class CompanyContextConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name='apps.company_context'

##############################################
"""from django.apps import AppConfig


class CompanyContextConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.company_context"

    def ready(self):
        from apps.company_context.infrastructure.utilities.tenant_database_loader import (
            TenantDatabaseLoader,
        )

        #TenantDatabaseLoader.load()"""

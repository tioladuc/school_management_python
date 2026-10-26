from urllib.parse import urlparse, unquote

from django.conf import settings
from django.db import connections

"""
class TenantDatabaseLoader:

    @classmethod
    def load(cls):
        
        #Load company aliases and connection strings into Django's
        #active database configuration.

        #Only runs when one database is configured initially.
        

        if len(settings.DATABASES) != 1:
            return

        from apps.company_context.infrastructure.orm.company_model import (
            CompanyModel,
        )

        companies = CompanyModel.objects.using("default").all()

        for company in companies:
            alias = company.alias
            connection_string = company.tenant_database

            if not alias or not connection_string:
                continue

            if alias == "default":
                continue

            database_config = cls.parse_connection_string(
                connection_string
            )

            # Add the configuration to Django's settings.
            settings.DATABASES[alias] = database_config

            # Update Django's active connection registry too.
            connections.databases[alias] = database_config

    @staticmethod
    def parse_connection_string(connection_string):
        parsed = urlparse(connection_string)
        scheme = parsed.scheme.lower()

        if scheme == "sqlite":
            if connection_string.startswith("sqlite:////"):
                database_name = parsed.path
            else:
                database_name = parsed.path.lstrip("/")

            return {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": database_name,
            }

        if scheme in ("postgres", "postgresql"):
            return {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": parsed.path.lstrip("/"),
                "USER": unquote(parsed.username or ""),
                "PASSWORD": unquote(parsed.password or ""),
                "HOST": parsed.hostname or "",
                "PORT": str(parsed.port or ""),
            }

        if scheme == "mysql":
            return {
                "ENGINE": "django.db.backends.mysql",
                "NAME": parsed.path.lstrip("/"),
                "USER": unquote(parsed.username or ""),
                "PASSWORD": unquote(parsed.password or ""),
                "HOST": parsed.hostname or "",
                "PORT": str(parsed.port or ""),
            }

        raise ValueError(
            f"Unsupported database connection scheme: {scheme}"
        )"""
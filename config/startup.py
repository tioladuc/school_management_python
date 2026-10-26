
# config/startup.py

# pip install "psycopg[binary]" mysqlclient mssql-django


import os
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs

from django.conf import settings
from django.db import connections


from pathlib import Path
from urllib.parse import urlparse, unquote, parse_qs

from django.conf import settings


def parse_connection_string(connection_string: str) -> dict:
    """
    Convert a database URL into a complete Django DATABASES configuration.
    Supports SQLite, PostgreSQL, MySQL, and SQL Server.
    """
    if not connection_string or not connection_string.strip():
        raise ValueError("The database connection string is empty.")

    connection_string = connection_string.strip()
    parsed = urlparse(connection_string)
    scheme = parsed.scheme.lower()

    # Standard Django database configuration defaults.
    config = {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "CONN_HEALTH_CHECKS": False,
        "OPTIONS": {},
        "TIME_ZONE": None,
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIGRATE": True,
            "MIRROR": None,
            "NAME": None,
        },
    }

    # SQLite
    if scheme == "sqlite":
        path = unquote(parsed.path)

        if not path:
            raise ValueError("The SQLite database path is empty.")

        if connection_string.startswith("sqlite:////"):
            # Absolute Linux path.
            database_name = path[1:]
        else:
            # Relative path under the project directory.
            database_name = str(
                Path(settings.BASE_DIR) / path.lstrip("/")
            )

        config.update({
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": database_name,
        })

        return config

    # PostgreSQL
    if scheme in ("postgres", "postgresql", "postgresql+psycopg"):
        engine = "django.db.backends.postgresql"

    # MySQL
    elif scheme in ("mysql", "mysql+pymysql"):
        engine = "django.db.backends.mysql"

    # SQL Server (requires mssql-django)
    elif scheme in ("mssql", "sqlserver"):
        engine = "mssql"

    else:
        raise ValueError(f"Unsupported database scheme: {scheme!r}")

    query = parse_qs(parsed.query)

    config.update({
        "ENGINE": engine,
        "NAME": unquote(parsed.path.lstrip("/")),
        "USER": unquote(parsed.username or ""),
        "PASSWORD": unquote(parsed.password or ""),
        "HOST": parsed.hostname or "",
        "PORT": str(parsed.port or ""),
    })

    if not config["NAME"]:
        raise ValueError(
            f"Database name is missing from {scheme!r} URL."
        )

    if "charset" in query:
        config["OPTIONS"] = {
            "charset": query["charset"][0],
        }

    if scheme in ("mssql", "sqlserver"):
        config["OPTIONS"] = {
            "driver": query.get(
                "driver", ["ODBC Driver 18 for SQL Server"]
            )[0],
        }

        if "extra_params" in query:
            config["OPTIONS"]["extra_params"] = (
                query["extra_params"][0]
            )

    return config


def parse_connection_string_top(connection_string: str) -> dict:
    """
    Convert a database URL into a Django DATABASES configuration.

    Supported schemes:
      sqlite:///relative/path.sqlite3
      sqlite:////absolute/path.sqlite3
      postgres://user:password@host:5432/database
      postgresql://user:password@host:5432/database
      mysql://user:password@host:3306/database
      mssql://user:password@host:1433/database

    SQL Server URLs are backend-specific; see the note below.

    sqlite:////home/tioladuc/projects/django_project/tenants/tenant001.sqlite3

    postgresql://tenant_user:password@localhost:5432/tenant001

    mysql://tenant_user:password@localhost:3306/tenant001

    mssql://tenant_user:password@localhost:1433/tenant001?driver=ODBC%20Driver%2018%20for%20SQL%20Server
    """

    if not connection_string or not connection_string.strip():
        raise ValueError("The database connection string is empty.")

    parsed = urlparse(connection_string)
    scheme = parsed.scheme.lower()

    # SQLite
    if scheme == "sqlite":
        if connection_string.startswith("sqlite:////"):
            database_name = unquote(parsed.path[1:])
        else:
            database_name = str(
                Path(settings.BASE_DIR) / unquote(parsed.path.lstrip("/"))
            )

        if not database_name:
            raise ValueError("The SQLite database path is empty.")

        return {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": database_name,
        }

    # PostgreSQL
    if scheme in ("postgres", "postgresql", "postgresql+psycopg"):
        engine = "django.db.backends.postgresql"

    # MySQL
    elif scheme in ("mysql", "mysql+pymysql"):
        engine = "django.db.backends.mysql"

    # SQL Server (requires mssql-django)
    elif scheme in ("mssql", "sqlserver"):
        engine = "mssql"

    else:
        raise ValueError(f"Unsupported database scheme: {scheme!r}")

    query = parse_qs(parsed.query)

    config = {
        "ENGINE": engine,
        "NAME": unquote(parsed.path.lstrip("/")),
        "USER": unquote(parsed.username or ""),
        "PASSWORD": unquote(parsed.password or ""),
        "HOST": parsed.hostname or "",
        "PORT": str(parsed.port or ""),
    }

    if not config["NAME"]:
        raise ValueError(f"Database name is missing from {scheme!r} URL.")

    # Optional query parameters.
    if "charset" in query:
        config["OPTIONS"] = {
            "charset": query["charset"][0]
        }

    if scheme in ("mssql", "sqlserver"):
        config["OPTIONS"] = {
            "driver": query.get(
                "driver", ["ODBC Driver 18 for SQL Server"]
            )[0],
        }

        if "extra_params" in query:
            config["OPTIONS"]["extra_params"] = query["extra_params"][0]

    return config


def load_tenant_databases() -> None:
    """
    Load tenant database configurations from the central company database.
    """
    print('duclair loading alias')
    # If tenant aliases already exist, do not load them again.
    if len(settings.DATABASES) != 1:
        return

    from apps.company_context.infrastructure.orm.company_model import (
        CompanyModel,
    )

    companies = (
        CompanyModel.objects.using("default")
        .exclude(alias="")
        .exclude(tenant_database="")
        .values_list("alias", "tenant_database")
    )

    for alias, tenant_database in companies:
        if not alias or alias == "default":
            continue

        database_config = parse_connection_string(tenant_database)

        # Register with Django's connection handler.
        settings.DATABASES[alias] = database_config
        connections.databases[alias] = database_config

    print(
        "Tenant database aliases loaded:",
        list(settings.DATABASES.keys()),
        list(settings.DATABASES.values()),
    )

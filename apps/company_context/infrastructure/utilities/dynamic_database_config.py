from copy import deepcopy
from uuid import uuid4
from django.db import connections
import traceback
from urllib.parse import urlparse, parse_qs, unquote

from sqlalchemy import alias

def configure_database_config(connection_string, alias=None):
    """
    Configure the database settings for the Django application.

    This function sets up the database configuration based on the provided
    connection string. It updates the default database settings in Django's
    connections.

    Raises
    ------
    ValueError
        If the connection string is empty or invalid.
    """
    if not connection_string:
        raise ValueError("connection_string cannot be empty.")

    # Create a copy of the default database configuration
    database_config = deepcopy(connections.databases["default"])
    
    # Update the configuration with the provided connection string
    database_config.update(_parse_connection_string(connection_string))
    
    # Register the updated configuration under a temporary alias
    if alias is None:
        alias = f"dynamic_db_{uuid4().hex}"
    connections.databases[alias] = database_config


# ============================================================
# CONNECTION STRING PARSER
# ============================================================

def _parse_connection_string(connection_string: str) -> dict:

    parsed = urlparse(connection_string)

    scheme = parsed.scheme.lower()

    # --------------------------------------------------------
    # SQLite
    # --------------------------------------------------------

    if scheme == "sqlite":

        database_name = parsed.path

        if database_name.startswith("/"):
            # sqlite:////home/user/db.sqlite3
            database_name = database_name

        else:
            # sqlite:///db.sqlite3
            database_name = database_name.lstrip("/")

        if not database_name:
            raise ValueError(
                "SQLite connection string must contain "
                "a database path."
            )

        return {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": database_name,
        }

    # --------------------------------------------------------
    # PostgreSQL
    # --------------------------------------------------------

    if scheme in (
        "postgresql",
        "postgres",
        "postgresql+psycopg",
        "postgresql+psycopg2",
    ):

        return {
            "ENGINE": "django.db.backends.postgresql",

            "NAME": parsed.path.lstrip("/"),

            "USER": unquote(
                parsed.username or ""
            ),

            "PASSWORD": unquote(
                parsed.password or ""
            ),

            "HOST": parsed.hostname or "",

            "PORT": str(
                parsed.port or ""
            ),
        }

    # --------------------------------------------------------
    # MySQL
    # --------------------------------------------------------

    if scheme in (
        "mysql",
        "mysql+pymysql",
        "mysql+mysqlconnector",
    ):

        return {
            "ENGINE": "django.db.backends.mysql",

            "NAME": parsed.path.lstrip("/"),

            "USER": unquote(
                parsed.username or ""
            ),

            "PASSWORD": unquote(
                parsed.password or ""
            ),

            "HOST": parsed.hostname or "",

            "PORT": str(
                parsed.port or ""
            ),
        }

    # --------------------------------------------------------
    # SQL Server
    # --------------------------------------------------------

    if scheme in (
        "mssql",
        "mssql+pyodbc",
    ):

        query = parse_qs(
            parsed.query
        )

        driver = query.get(
            "driver",
            ["ODBC Driver 18 for SQL Server"],
        )[0]

        options = {
            "driver": driver,
        }

        # Optional SQL Server parameters.
        if "TrustServerCertificate" in query:
            options["TrustServerCertificate"] = (
                query["TrustServerCertificate"][0]
            )

        if "Encrypt" in query:
            options["Encrypt"] = (
                query["Encrypt"][0]
            )

        return {
            "ENGINE": "mssql",

            "NAME": parsed.path.lstrip("/"),

            "USER": unquote(
                parsed.username or ""
            ),

            "PASSWORD": unquote(
                parsed.password or ""
            ),

            "HOST": parsed.hostname or "",

            "PORT": str(
                parsed.port or ""
            ),

            "OPTIONS": options,
        }

    raise ValueError(
        f"Unsupported database type: {scheme}"
    )


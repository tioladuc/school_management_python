from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote
from uuid import uuid4

from django.db import connections, transaction

from apps.company_context.infrastructure.utilities.create_company_db import create_database
from apps.company_context.infrastructure.utilities.create_tables_company import create_tables
from apps.company_context.infrastructure.utilities.dynamic_database_config import configure_database_config
from apps.company_context.infrastructure.utilities.insert_data_tables import insert_data

from apps.company_context.infrastructure.utilities.script_company_creation import (
    produce_tables_models_for_company_tocreate,
    produce_data_to_insert_base_company,
)
from apps.company_context.infrastructure.utilities.script_school_creation import (
    produce_tables_models_for_school_tocreate,
    produce_data_to_insert_for_school,
)
from apps.company_context.infrastructure.utilities.drop_tables_db_company import (
    delete_model_tables,
    delete_database,
    do_backup_company_database,
)

def preparer_company_database(connection_string: str) -> dict:
    """
    Prepare a company database by creating tables and inserting data.

    Parameters
    ----------
    connection_string:
        Database URL identifying the target database.
        """
    create_database(connection_string)

    alias = f"dynamic_db_{uuid4().hex}"
    configure_database_config(connection_string, alias)

    data = produce_tables_models_for_company_tocreate()
    create_tables(alias, data)
    insert_data(alias, produce_data_to_insert_base_company())

    connections[alias].close()
    connections.databases.pop(alias, None)


def preparer_tables_for_school(connection_string: str) -> dict:
    """
    Prepare a company database by creating tables and inserting data.

    Parameters
    ----------
    connection_string:
        Database URL identifying the target database.
        """
    
    alias = f"dynamic_db_{uuid4().hex}"
    configure_database_config(connection_string, alias)

    data = produce_tables_models_for_school_tocreate()
    create_tables(alias, data)
    
    connections[alias].close()
    connections.databases.pop(alias, None)


def preparer_data_for_school(connection_string: str) -> dict:
    """
    Prepare a company database by creating tables and inserting data.

    Parameters
    ----------
    connection_string:
        Database URL identifying the target database.
        """

    alias = f"dynamic_db_{uuid4().hex}"
    configure_database_config(connection_string, alias)
    
    insert_data(alias, produce_data_to_insert_for_school())

    connections[alias].close()
    connections.databases.pop(alias, None)


def drop_database(connection_string: str) -> None:
    """
    Drop a database.

    Parameters
    ----------
    connection_string:
        Database URL identifying the target database.
        """
    alias = f"dynamic_db_{uuid4().hex}"
    configure_database_config(connection_string, alias)

    data_company = produce_tables_models_for_company_tocreate()
    data_school = produce_tables_models_for_school_tocreate()
    delete_model_tables( alias, data_school)
    delete_model_tables( alias, data_company)

    delete_database( alias, connection_string, {})
    
    connections[alias].close()
    connections.databases.pop(alias, None)


def backup_company_database(connection_string: str) -> None:
    """
    Backup the company database.

    Parameters
    ----------
    connection_string:
        Database URL identifying the target database.
        """
    alias = f"dynamic_db_{uuid4().hex}"
    configure_database_config(connection_string, alias)
    
    do_backup_company_database( alias, connection_string, {})
    
    connections[alias].close()
    connections.databases.pop(alias, None)


def preparer_data_for_school_from_another_school(connection_string: str, school_code: str) -> dict:
    """
    Prepare a company database by creating tables and inserting data.

    Parameters
    ----------
    connection_string:
        Database URL identifying the target database.
        """

    alias = f"dynamic_db_{uuid4().hex}"
    configure_database_config(connection_string, alias)

    insert_data(alias, produce_data_to_insert_for_school())

    connections[alias].close()
    connections.databases.pop(alias, None)

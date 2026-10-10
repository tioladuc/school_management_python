from ast import alias
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote
from uuid import uuid4

from django.db import connection, connections


def delete_database(
    alias: str,
    connection_string: str,
    model_classes: list,
) -> None:
    """
    Delete the specified Django model tables and then delete
    the database itself.

    Supported:
        - SQLite
        - PostgreSQL
        - MySQL
        - SQL Server

    Parameters
    ----------
    connection_string:
        Connection string identifying the database.

    model_classes:
        List of Django model classes whose tables should be
        deleted before dropping the database.

    WARNING:
        This operation is destructive and cannot be undone.
    """

    if not connection_string:
        raise ValueError(
            "connection_string cannot be empty."
        )

    if not model_classes:
        raise ValueError(
            "model_classes cannot be empty."
        )

    connection = connections[alias]
    delete_model_tables( connection, model_classes)

    engine = _detect_engine(connection_string)

    if engine == "sqlite":
        _delete_sqlite_database(
            connection,
            model_classes,
        )
        return

    if engine == "postgresql":
        _delete_postgresql_database(
            connection,
            model_classes,
        )
        return

    if engine == "mysql":
        _delete_mysql_database(
            connection,
            model_classes,
        )
        return

    if engine == "mssql":
        _delete_sqlserver_database(
            connection,
            model_classes,
        )
        return

    raise ValueError(
        f"Unsupported database engine: {engine}"
    )

# ============================================================
# DELETE DJANGO TABLES
# ============================================================

def delete_model_tables(
    alias,
    model_classes,
):
    """
    Delete the supplied Django model tables.

    Models are processed in reverse order so that tables
    containing foreign keys are normally removed before the
    tables they depend on.
    """
    connection = connections[alias]
    existing_tables = set(
        connection.introspection.table_names()
    )

    # Reverse order to help with FK dependencies.
    for model_class in reversed(model_classes):

        _validate_model(model_class)

        table_name = model_class._meta.db_table

        if table_name not in existing_tables:
            continue

        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(
                model_class
            )

        existing_tables.remove(table_name)

# ============================================================
# DELETE DJANGO TABLES
# ============================================================

def do_backup_company_database(
    alias,
):
    """
    Backup the company database.

    """
    connection = connections[alias]
    existing_tables = set(
        connection.introspection.table_names()
    )

    # do the back up of the database
   


# ============================================================
# ENGINE
# ============================================================

def _detect_engine(connection_string: str) -> str:

    scheme = urlparse(
        connection_string
    ).scheme.lower()

    if scheme == "sqlite":
        return "sqlite"

    if scheme in (
        "postgresql",
        "postgres",
        "postgresql+psycopg",
        "postgresql+psycopg2",
    ):
        return "postgresql"

    if scheme in (
        "mysql",
        "mysql+pymysql",
        "mysql+mysqlconnector",
    ):
        return "mysql"

    if scheme in (
        "mssql",
        "mssql+pyodbc",
    ):
        return "mssql"

    raise ValueError(
        f"Unsupported database scheme: {scheme}"
    )

# ============================================================
# SQLITE
# ============================================================

def _delete_sqlite_database(
    database_config,
):

    database_path = database_config["NAME"]

    if not database_path:
        raise ValueError(
            "SQLite database path is missing."
        )

    path = Path(
        database_path
    ).expanduser()

    if not path.exists():
        return

    # Delete the actual SQLite database file.
    if path.exists():
        path.unlink()

# ============================================================
# POSTGRESQL
# ============================================================

def _delete_postgresql_database(
    database_config,
):

    database_name = database_config["NAME"]

    if not database_name:
        raise ValueError(
            "PostgreSQL database name is missing."
        )

    # First connect to the target database.
    target_alias = (
        f"delete_postgres_target_{uuid4().hex}"
    )

    connections.databases[target_alias] = database_config

    # Now connect to postgres database to DROP DATABASE.
    admin_config = database_config.copy()
    admin_config["NAME"] = "postgres"

    admin_alias = (
        f"delete_postgres_admin_{uuid4().hex}"
    )

    connections.databases[admin_alias] = admin_config

    admin_connection = connections[
        admin_alias
    ]

    try:

        # PostgreSQL cannot drop a database while connections
        # to it remain open.
        quoted_database = (
            admin_connection
            .ops
            .quote_name(database_name)
        )

        admin_connection.close()

        # Use a direct database driver connection would normally
        # be preferable here because DROP DATABASE cannot run
        # inside a transaction.
        #
        # Django's PostgreSQL connection can be configured with
        # AUTOCOMMIT for this operation.

        admin_connection = connections[
            admin_alias
        ]

        admin_connection.set_autocommit(
            True
        )

        with admin_connection.cursor() as cursor:

            cursor.execute(
                f"DROP DATABASE IF EXISTS "
                f"{quoted_database}"
            )

    finally:

        admin_connection.close()

        connections.databases.pop(
            admin_alias,
            None,
        )

# ============================================================
# MYSQL
# ============================================================

def _delete_mysql_database(
    database_config,
):

    database_name = database_config["NAME"]

    if not database_name:
        raise ValueError(
            "MySQL database name is missing."
        )

    # Connect to target database.
    target_alias = (
        f"delete_mysql_target_{uuid4().hex}"
    )

    connections.databases[target_alias] = database_config

    # Connect to MySQL server without selecting database.
    admin_config = database_config.copy()
    admin_config["NAME"] = ""

    admin_alias = (
        f"delete_mysql_admin_{uuid4().hex}"
    )

    connections.databases[admin_alias] = admin_config

    admin_connection = connections[
        admin_alias
    ]

    try:

        quoted_database = (
            admin_connection
            .ops
            .quote_name(database_name)
        )

        with admin_connection.cursor() as cursor:

            cursor.execute(
                f"DROP DATABASE IF EXISTS "
                f"{quoted_database}"
            )

    finally:

        admin_connection.close()

        connections.databases.pop(
            admin_alias,
            None,
        )

# ============================================================
# SQL SERVER
# ============================================================

def _delete_sqlserver_database(
    database_config,
):

    database_name = database_config["NAME"]

    if not database_name:
        raise ValueError(
            "SQL Server database name is missing."
        )

    # Delete the Django tables first.
    target_alias = (
        f"delete_mssql_target_{uuid4().hex}"
    )

    connections.databases[target_alias] = database_config

    # Connect to master.
    admin_config = database_config.copy()
    admin_config["NAME"] = "master"

    admin_alias = (
        f"delete_mssql_admin_{uuid4().hex}"
    )

    connections.databases[admin_alias] = admin_config

    admin_connection = connections[
        admin_alias
    ]

    try:

        quoted_database = (
            admin_connection
            .ops
            .quote_name(database_name)
        )

        escaped_name = (
            database_name.replace("'", "''")
        )

        with admin_connection.cursor() as cursor:

            cursor.execute(
                f"""
                IF DB_ID(N'{escaped_name}') IS NOT NULL
                BEGIN
                    ALTER DATABASE {quoted_database}
                    SET SINGLE_USER
                    WITH ROLLBACK IMMEDIATE;

                    DROP DATABASE {quoted_database};
                END
                """
            )

    finally:

        admin_connection.close()

        connections.databases.pop(
            admin_alias,
            None,
        )

# ============================================================
# MODEL VALIDATION
# ============================================================

def _validate_model(model_class):

    meta = model_class._meta

    if meta.abstract:
        raise ValueError(
            f"Cannot delete table for abstract model "
            f"'{model_class.__name__}'."
        )

    if meta.proxy:
        raise ValueError(
            f"Cannot delete table for proxy model "
            f"'{model_class.__name__}'."
        )

    if not meta.managed:
        raise ValueError(
            f"Model '{model_class.__name__}' has "
            f"managed=False."
        )
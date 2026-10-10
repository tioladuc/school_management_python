from pathlib import Path
from urllib.parse import urlparse

from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url


def create_database(connection_string: str) -> dict:
    """
    Create an empty database from a database connection string.

    Supported:
        - SQLite
        - PostgreSQL
        - MySQL
        - SQL Server

    The database is created with NO tables.

    Returns:
        {
            "created": bool,
            "database": str,
            "engine": str,
            "message": str,
        }
    """

    if not connection_string:
        raise ValueError("connection_string cannot be empty.")

    url = make_url(connection_string)

    engine_name = url.get_backend_name()

    if engine_name in ("sqlite",):
        return _create_sqlite_database(url)

    if engine_name in ("postgresql", "postgres"):
        return _create_postgresql_database(url)

    if engine_name == "mysql":
        return _create_mysql_database(url)

    if engine_name in ("mssql", "sqlserver"):
        return _create_sqlserver_database(url)

    raise ValueError(
        f"Unsupported database engine: {engine_name}"
    )


# ============================================================
# SQLite
# ============================================================

def _create_sqlite_database(url):
    database_path = url.database

    if not database_path:
        raise ValueError(
            "SQLite connection string must contain a database path."
        )

    path = Path(database_path).expanduser()

    # If the database already exists, don't modify it.
    if path.exists():
        return {
            "created": False,
            "database": str(path),
            "engine": "sqlite",
            "message": "SQLite database already exists.",
        }

    # Make sure the parent directory exists.
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # sqlite3 creates the file when connecting.
    engine = create_engine(
        url,
        connect_args={
            "check_same_thread": False,
        },
    )

    try:
        with engine.connect():
            pass

    finally:
        engine.dispose()

    return {
        "created": True,
        "database": str(path),
        "engine": "sqlite",
        "message": "SQLite database created successfully.",
    }


# ============================================================
# PostgreSQL
# ============================================================

def _create_postgresql_database(url):

    database_name = url.database

    if not database_name:
        raise ValueError(
            "PostgreSQL connection string must contain a database name."
        )

    # PostgreSQL needs us to connect to an existing database
    # before creating the target database.
    admin_url = url.set(
        database="postgres"
    )

    engine = create_engine(
        admin_url,
        isolation_level="AUTOCOMMIT",
    )

    try:

        with engine.connect() as connection:

            exists = connection.execute(
                text(
                    """
                    SELECT 1
                    FROM pg_database
                    WHERE datname = :database_name
                    """
                ),
                {
                    "database_name": database_name,
                },
            ).scalar()

            if exists:

                return {
                    "created": False,
                    "database": database_name,
                    "engine": "postgresql",
                    "message": "PostgreSQL database already exists.",
                }

            # Quote the database identifier safely.
            quoted_name = (
                connection.dialect.identifier_preparer
                .quote(database_name)
            )

            connection.exec_driver_sql(
                f"CREATE DATABASE {quoted_name}"
            )

    finally:
        engine.dispose()

    return {
        "created": True,
        "database": database_name,
        "engine": "postgresql",
        "message": "PostgreSQL database created successfully.",
    }


# ============================================================
# MySQL
# ============================================================

def _create_mysql_database(url):

    database_name = url.database

    if not database_name:
        raise ValueError(
            "MySQL connection string must contain a database name."
        )

    # Remove database from connection URL so we connect to
    # the MySQL server rather than to the database being created.
    admin_url = url.set(
        database=None
    )

    engine = create_engine(
        admin_url,
        isolation_level="AUTOCOMMIT",
    )

    try:

        with engine.connect() as connection:

            quoted_name = (
                connection.dialect.identifier_preparer
                .quote(database_name)
            )

            connection.exec_driver_sql(
                f"CREATE DATABASE IF NOT EXISTS {quoted_name}"
            )

            # Determine whether it existed or was just created.
            exists = connection.execute(
                text(
                    """
                    SELECT SCHEMA_NAME
                    FROM INFORMATION_SCHEMA.SCHEMATA
                    WHERE SCHEMA_NAME = :database_name
                    """
                ),
                {
                    "database_name": database_name,
                },
            ).scalar()

            if exists:

                return {
                    "created": True,
                    "database": database_name,
                    "engine": "mysql",
                    "message": (
                        "MySQL database exists or was created successfully."
                    ),
                }

    finally:
        engine.dispose()

    return {
        "created": False,
        "database": database_name,
        "engine": "mysql",
        "message": "Unable to create MySQL database.",
    }


# ============================================================
# SQL Server
# ============================================================

def _create_sqlserver_database(url):

    database_name = url.database

    if not database_name:
        raise ValueError(
            "SQL Server connection string must contain a database name."
        )

    # SQL Server has a master database that we can connect to
    # before creating the target database.
    admin_url = url.set(
        database="master"
    )

    engine = create_engine(
        admin_url,
        isolation_level="AUTOCOMMIT",
    )

    try:

        with engine.connect() as connection:

            quoted_name = (
                connection.dialect.identifier_preparer
                .quote(database_name)
            )

            connection.exec_driver_sql(
                f"""
                IF DB_ID(N'{database_name.replace("'", "''")}') IS NULL
                BEGIN
                    CREATE DATABASE {quoted_name}
                END
                """
            )

            return {
                "created": True,
                "database": database_name,
                "engine": "mssql",
                "message": (
                    "SQL Server database exists or was created successfully."
                ),
            }

    finally:
        engine.dispose()
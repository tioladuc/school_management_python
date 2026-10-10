import traceback

from django.db import connections

from apps.company_context.infrastructure.utilities.dynamic_database_config import configure_database_config


def create_tables(alias: str, model_classes: list) -> None:
    """
    Create database tables for the supplied Django models.

    Parameters
    ----------
    connection_string:
        Database connection URL.

    model_classes:
        List of Django model classes.

    Supported database types:
        - SQLite
        - PostgreSQL
        - MySQL
        - SQL Server

    Example
    -------
    create_tables(
        "postgresql://user:password@localhost:5432/tenant001",
        [
            SchoolModel,
            EmployeeModel,
            StaffModel,
        ],
    )
    """
        
    connection = connections[alias]
    
    try:
        
        with connection.schema_editor() as schema_editor:
            existing_tables = set(
                connection.introspection.table_names()
            )
            
            for model_class in model_classes:
                _validate_model(model_class)
                table_name = model_class._meta.db_table

                if table_name in existing_tables:
                    continue

                schema_editor.create_model(
                    model_class
                )

                existing_tables.add(table_name)
    except Exception as x:        
        print(x) 
        traceback.print_exc()
    finally:
        connection.close()

        # Remove our temporary connection configuration.
        connections.databases.pop(
            alias,
            None
        )

# ============================================================
# MODEL VALIDATION
# ============================================================

def _validate_model(model_class):

    meta = model_class._meta

    if meta.abstract:
        raise ValueError(
            f"Cannot create table for abstract model "
            f"'{model_class.__name__}'."
        )

    if meta.proxy:
        raise ValueError(
            f"Cannot create table for proxy model "
            f"'{model_class.__name__}'."
        )

    if not meta.managed:
        raise ValueError(
            f"Model '{model_class.__name__}' has "
            f"managed=False."
        )
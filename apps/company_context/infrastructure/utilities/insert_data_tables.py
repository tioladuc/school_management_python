from pathlib import Path

from django.db import connections, transaction

from apps.company_context.infrastructure.utilities.dynamic_database_config import configure_database_config


def insert_data(alias: str, model_data: list) -> dict:
    """
    Insert data into tables belonging to multiple Django models.

    Parameters
    ----------
    connection_string:
        Database URL identifying the target database.

    model_data:
        List of dictionaries containing:
            - model: Django model class
            - records: list of dictionaries representing records

    Example
    -------
    insert_data(
        connection_string,
        [
            {
                "model": SchoolModel,
                "records": [
                    {"code": "SCH001", "name": "Primary School"},
                ],
            },
            {
                "model": EmployeeModel,
                "records": [
                    {"first_name": "John", "last_name": "Smith"},
                ],
            },
        ],
    )

    Returns
    -------
    Dictionary containing the number of inserted records.
    """
    connection = connections[alias]
    total_inserted = 0
    details = []

    try:
        # Validate the payload before writing anything.
        for item in model_data:
            
            if not isinstance(item, dict):
                raise TypeError("Each model_data item must be a dictionary.")
            
            model = item.get("model")
            records = item.get("records")
            
            if not isinstance(model, type) or not hasattr(model, "_meta"):
                raise TypeError("'model' must be a Django model class.")
            
            if model._meta.abstract or model._meta.proxy:
                raise ValueError(
                    f"{model.__name__} must be a concrete, non-proxy model."
                )
            
            if not model._meta.managed:
                raise ValueError(f"{model.__name__} has managed=False.")
            
            if not isinstance(records, list):
                raise TypeError(f"'records' must be a list for {model.__name__}.")
            
            for record in records:
                if not isinstance(record, dict):
                    raise TypeError(
                        f"Every record for {model.__name__} " "must be a dictionary."
                    )
            
        # Check that the required tables already exist.
        existing_tables = set(connection.introspection.table_names())
        
        for item in model_data:
            model = item["model"]
            table_name = model._meta.db_table

            if table_name not in existing_tables:
                raise ValueError(
                    f"Table '{table_name}' does not exist " f"in the target database."
                )

        # All inserts share one transaction.
        with transaction.atomic(using=alias):
            for item in model_data:
                model = item["model"]
                records = item["records"]
                
                if not records:
                    details.append(
                        {
                            "model": model.__name__,
                            "inserted": 0,
                        }
                    )
                    continue
                objects = [model(**record) for record in records]
                # Bulk insert through the selected database.
                model.objects.using(alias).bulk_create(objects)
                count = len(objects)
                total_inserted += count
                details.append(
                    {
                        "model": model.__name__,
                        "table": model._meta.db_table,
                        "inserted": count,
                    }
                )
        
        print({
            "inserted": total_inserted,
            "details": details,
        })
        return {
            "inserted": total_inserted,
            "details": details,
        }
    except Exception as e:
        print('insert_data exception', e)
        raise 
    finally:
        connection.close()
        del connections[alias]
        connections.databases.pop(alias, None)


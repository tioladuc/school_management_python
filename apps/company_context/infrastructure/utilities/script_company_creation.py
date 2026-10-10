


from apps.company_context.infrastructure.orm.staff_model import StaffModel


def produce_tables_models_for_company_tocreate() -> list:
    """
    Produce a list of Django model classes to create tables for.

    Returns
    -------
    List of Django model classes.
    """
    
    from apps.company_context.infrastructure.orm.models import (
        SchoolModel,
        StaffModel,
    )
    
    return [
        SchoolModel,
        StaffModel,
    ]





def produce_data_to_insert_base_company() -> list:
    """
    Produce a list of data to insert into the database.

    Returns
    -------
    List of dictionaries containing model classes and records.
    """

    from apps.company_context.infrastructure.orm.models import (
        SchoolModel,
    )

    return [
        {
            "model": SchoolModel,
            "records": [
                {
                    "code": "SCH001",
                    "name": "Primary School",
                    "city": "Lagos",
                    "country": "Nigeria",
                    "status": "ACTIVE",
                },
                {
                    "code": "SCH002",
                    "name": "Secondary School",
                    "city": "Abuja",
                    "country": "Nigeria",
                    "status": "ACTIVE",
                },
                {
                    "code": "SCH003",
                    "name": "Community School",
                    "city": "Ibadan",
                    "country": "Nigeria",
                    "status": "SUSPENDED",
                },
                {
                    "code": "SCH004",
                    "name": "International School",
                    "city": "Accra",
                    "country": "Ghana",
                    "status": "ACTIVE",
                },
            ],
        },        
        {
            "model": StaffModel,
            "records": [
                {
                    "staff_number": "STF001",
                    "first_name": "Amina",
                    "last_name": "Okafor",
                    "email": "amina.okafor@example.com",
                    "phone": "+2348012345001",
                    "position": "Administrator",
                    "status": "ACTIVE",
                },
                {
                    "staff_number": "STF002",
                    "first_name": "Daniel",
                    "last_name": "Mensah",
                    "email": "daniel.mensah@example.com",
                    "phone": "+2348012345002",
                    "position": "Teacher",
                    "status": "ACTIVE",
                },
                {
                    "staff_number": "STF003",
                    "first_name": "Grace",
                    "last_name": "Bello",
                    "email": "grace.bello@example.com",
                    "phone": "+2348012345003",
                    "position": "Accountant",
                    "status": "SUSPENDED",
                },
                {
                    "staff_number": "STF004",
                    "first_name": "Samuel",
                    "last_name": "Adeyemi",
                    "email": "samuel.adeyemi@example.com",
                    "phone": "+2348012345004",
                    "position": "Guidance Counselor",
                    "status": "ACTIVE",
                },
            ],
        },
    ]

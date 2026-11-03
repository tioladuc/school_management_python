

def produce_tables_models_for_school_tocreate() -> list:
    """
    Produce a list of Django model classes to create tables for.

    Returns
    -------
    List of Django model classes.
    """
    
    from apps.company_context.infrastructure.orm.models import (
        AcademicYearModel,
        ClassGroupModel,
        SubjectGroupModel,
        SubjectModel,
        StaffModel,
    )
    
    return [
        AcademicYearModel,
        ClassGroupModel,
        SubjectGroupModel,
        SubjectModel,
        StaffModel,
    ]



def produce_data_to_insert_for_school() -> list:
    """
    Produce sample data to insert into the tenant database.

    Returns
    -------
    List of dictionaries containing model classes and records.
    """

    from apps.company_context.infrastructure.orm.models import (
        SchoolModel,
        StaffModel,
    )

    print("Producing data to insert for school...++++++++++++++++")

    return [
        {
            "model": SchoolModel,
            "records": [
                {
                    "code": "SCH001",
                    "name_fr": "École primaire",
                    "name_en": "Primary School",
                    "phone": "+2348012345001",
                    "email": "info.sch001@example.com",
                    "address": "12 Lagos Street",
                    "autorization": "AUTH-SCH001",
                    "founder": "Amina Okafor",
                    "principal": "Daniel Mensah",
                    "city": "Lagos",
                    "country": "Nigeria",
                    "status": "ACTIVE",
                },
                {
                    "code": "SCH002",
                    "name_fr": "École secondaire",
                    "name_en": "Secondary School",
                    "phone": "+2348012345002",
                    "email": "info.sch002@example.com",
                    "address": "25 Abuja Avenue",
                    "autorization": "AUTH-SCH002",
                    "founder": "Grace Bello",
                    "principal": "Samuel Adeyemi",
                    "city": "Abuja",
                    "country": "Nigeria",
                    "status": "ACTIVE",
                },
                {
                    "code": "SCH003",
                    "name_fr": "École communautaire",
                    "name_en": "Community School",
                    "phone": "+2348012345003",
                    "email": "info.sch003@example.com",
                    "address": "8 Ibadan Road",
                    "autorization": "AUTH-SCH003",
                    "founder": "Samuel Adeyemi",
                    "principal": "Amina Okafor",
                    "city": "Ibadan",
                    "country": "Nigeria",
                    "status": "SUSPENDED",
                },
                {
                    "code": "SCH004",
                    "name_fr": "École internationale",
                    "name_en": "International School",
                    "phone": "+2332012345004",
                    "email": "info.sch004@example.com",
                    "address": "15 Accra Avenue",
                    "autorization": "AUTH-SCH004",
                    "founder": "Daniel Mensah",
                    "principal": "Grace Bello",
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





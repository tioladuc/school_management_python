

def produce_tables_models_for_school_tocreate_todelete() -> list:
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


def produce_tables_models_for_school_tocreate() -> list:
    """
    Produce Django model classes in dependency order, from the
    least dependent to the most dependent.

    Returns
    -------
    list[type[models.Model]]
        Ordered list of Django model classes.
    """

    from apps.company_context.infrastructure.orm.models import (
        # School and basic entities
        SchoolModel,
        StaffModel,
        StudentModule,
        ParentModule,

        # School academic structure
        AcademicYearModel,
        BookCategoryModel,
        FeeCategoryModel,
        StudentParentModule,

        # Contracts and subscriptions
        ContractModel,
        ContractDataModel,
        SubscriptionModel,

        # Library
        BookModel,

        # Staff and academic organization
        YearlyStaffModel,
        ClassGroupModel,
        TermModel,
        SubjectGroupModel,
        ClassRoomModel,
        YearlyStudentModel,
        SubjectModel,

        # Library bookings
        BookingModel,

        # Fees
        FeeLibraryModel,
        FeeOnlineCourseModel,
        FeeLibraryPaymentModel,
        FeeOnlineCoursePaymentModel,

        # Finance
        FinanceCategoryModel,
        FinanceSubCategoryModel,
        FinanceItemModel,
        FinanceEntryModel,

        # Payroll
        PayCategoryModel,
        PayRecursiveItem,
        PayStaticItem,
        PayRecursiveItemData,
        PayStaticItemData,

        # Academic sequences and assessments
        SequenceModel,
        AssessmentModel,
        ModuleYearModel,
        ModuleTermModel,
        ModuleSequenceModel,
        ModuleAssessmentModel,

        # Instalments and payments
        InstalmentModel,
        InstalmentBaseModel,
        PaymentModel,
        PaymentInstalmentModel,
        MoratoryModel,

        # Student discipline
        DisciplineModel,
        DisciplineYearModel,
        DisciplineTermModel,
        DisciplineSequenceModel,
        DisciplineAssessmentModel,

        # Student academic records
        NoteModel,
        ClassRollModel,
        StudentMessageModel,
        StudentMoveScanModel,

        # Online courses
        OnlineCourseModel,
        OnlineCourseAssessmentModel,
        OnlineCourseReadingModel,
        OnlineCourseAssessmentAnswerModel,
    )

    return [
        # 1. Independent entities
        SchoolModel,
        StaffModel,
        StudentModule,
        ParentModule,

        # 2. Basic school entities
        AcademicYearModel,
        BookCategoryModel,
        FeeCategoryModel,
        StudentParentModule,

        # 3. Contracts and subscriptions
        # ContractModel,
        # ContractDataModel,
        # SubscriptionModel,

        # 4. Library
        BookModel,

        # 5. Staff and academic organization
        YearlyStaffModel,
        ClassGroupModel,
        TermModel,
        SubjectGroupModel,
        ClassRoomModel,
        YearlyStudentModel,
        SubjectModel,

        # 6. Library bookings
        BookingModel,

        # 7. Fees
        FeeLibraryModel,
        FeeOnlineCourseModel,
        FeeLibraryPaymentModel,
        FeeOnlineCoursePaymentModel,

        # 8. Finance
        FinanceCategoryModel,
        FinanceSubCategoryModel,
        FinanceItemModel,
        FinanceEntryModel,

        # 9. Payroll
        PayCategoryModel,
        PayRecursiveItem,
        PayStaticItem,
        PayRecursiveItemData,
        PayStaticItemData,

        # 10. Academic sequences and assessments
        SequenceModel,
        AssessmentModel,
        ModuleYearModel,
        ModuleTermModel,
        ModuleSequenceModel,
        ModuleAssessmentModel,

        # 11. Instalments and payments
        InstalmentModel,
        InstalmentBaseModel,
        PaymentModel,
        PaymentInstalmentModel,
        MoratoryModel,

        # 12. Student discipline
        DisciplineModel,
        DisciplineYearModel,
        DisciplineTermModel,
        DisciplineSequenceModel,
        DisciplineAssessmentModel,

        # 13. Student academic records
        NoteModel,
        ClassRollModel,
        StudentMessageModel,
        StudentMoveScanModel,

        # 14. Online courses
        OnlineCourseModel,
        OnlineCourseAssessmentModel,
        OnlineCourseReadingModel,
        OnlineCourseAssessmentAnswerModel,
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





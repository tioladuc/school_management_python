from django.db import models

from .company_model import CompanyModel
from .school_model import SchoolModel
from .staff_model import StaffModel
from .contract_model import ContractModel
from .contract_data_model import ContractDataModel
from .subscription_model import SubscriptionModel

from .parent_model import ParentModule
from .student_module import StudentModule
from .student_parent_module import StudentParentModule
from .academic_year_model import AcademicYearModel
from .class_group_model import ClassGroupModel
from .class_room_model import ClassRoomModel
from .yearly_student_model import YearlyStudentModel
from .subject_group_model import SubjectGroupModel
from .yearly_staff_model import YearlyStaffModel
from .subject_model import SubjectModel
from .term_model import TermModel
from .sequence_model import SequenceModel
from .assessment_model import AssessmentModel
from .note_model import NoteModel
from .module_year_model import ModuleYearModel
from .module_term_model import ModuleTermModel
from .module_sequence_model import ModuleSequenceModel
from .module_assessment_model import ModuleAssessmentModel
from .instalment_model import InstalmentModel
from .instalment_base_model import InstalmentBaseModel
from .payment_model import PaymentModel
from .payment_instalment_model import PaymentInstalmentModel
from .moratory_model import MoratoryModel
from .discipline_model import DisciplineModel
from .discipline_year_model import DisciplineYearModel
from .discipline_term_model import DisciplineTermModel
from .discipline_sequence_model import DisciplineSequenceModel
from .discipline_assessment_model import DisciplineAssessmentModel

from .finance_category_model import FinanceCategoryModel
from .finance_subcategory_model import FinanceSubCategoryModel
from .finance_item_model import FinanceItemModel
from .finance_entry_model import FinanceEntryModel
from .pay_category_model import PayCategoryModel
from .pay_recursive_item_model import PayRecursiveItem
from .pay_static_item_model import PayStaticItem
from .pay_recursive_item_data_model import PayRecursiveItemData
from .pay_static_item_data_model import PayStaticItemData

from .class_roll_model import ClassRollModel
from .student_message_model import StudentMessageModel
from .student_move_scan_model import StudentMoveScanModel
from .book_category_model import BookCategoryModel
from .book_model import BookModel
from .booking_model import BookingModel

from .fee_category_model import FeeCategoryModel
from .fee_library_model import FeeLibraryModel
from .fee_online_course_model import FeeOnlineCourseModel
from .fee_library_payment_model import FeeLibraryPaymentModel
from .fee_online_course_payment_model import FeeOnlineCoursePaymentModel
from .online_course_model import OnlineCourseModel
from .online_course_assessment_model import OnlineCourseAssessmentModel
from .online_course_reading_model import OnlineCourseReadingModel
from .online_course_assessment_answer_model import OnlineCourseAssessmentAnswerModel

__all__ = [
    "CompanyModel",
    "SchoolModel",
    "StaffModel",
    "ContractModel",
    "ContractDataModel",
    "SubscriptionModel",


    "ParentModule",
    "StudentModule",
    "StudentParentModule",
    "AcademicYearModel",
    "ClassGroupModel",
    "ClassRoomModel",
    "YearlyStudentModel",   
    "SubjectGroupModel",
    "YearlyStaffModel",
    "SubjectModel",
    "TermModel",
    "SequenceModel",
    "AssessmentModel",
    "NoteModel",
    "ModuleYearModel",
    "ModuleTermModel",
    "ModuleSequenceModel",
    "ModuleAssessmentModel",
    "InstalmentModel",
    "InstalmentBaseModel",
    "PaymentModel",
    "PaymentInstalmentModel",
    "MoratoryModel",
    "DisciplineModel",
    "DisciplineYearModel",
    "DisciplineTermModel",
    "DisciplineSequenceModel",
    "DisciplineAssessmentModel",

    "FinanceCategoryModel",
    "FinanceSubCategoryModel",
    "FinanceItemModel",
    "FinanceEntryModel",
    "PayCategoryModel",
    "PayRecursiveItem",
    "PayStaticItem",
    "PayRecursiveItemData",
    "PayStaticItemData",

    "ClassRollModel",
    "StudentMessageModel",
    "StudentMoveScanModel",
    "BookCategoryModel",
    "BookModel",
    "BookingModel",

    "FeeCategoryModel",
    "FeeLibraryModel",
    "FeeOnlineCourseModel",
    "FeeLibraryPaymentModel",
    "FeeOnlineCoursePaymentModel",
    "OnlineCourseModel",
    "OnlineCourseAssessmentModel",
    "OnlineCourseReadingModel",
    "OnlineCourseAssessmentAnswerModel",

]

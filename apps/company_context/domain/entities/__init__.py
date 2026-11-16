"""Domain entities generated from the supplied Django ORM models."""

from .academic_year import AcademicYear
from .assessment import Assessment
from .booking import Booking
from .book_category import BookCategory
from .book import Book
from .class_group import ClassGroup
from .class_roll import ClassRoll
from .class_room import ClassRoom
from .contract_data import ContractData
from .discipline_assessment import DisciplineAssessment
from .discipline import Discipline
from .discipline_sequence import DisciplineSequence
from .discipline_term import DisciplineTerm
from .discipline_year import DisciplineYear
from .fee_category import FeeCategory
from .fee_library import FeeLibrary
from .fee_library_payment import FeeLibraryPayment
from .fee_online_course import FeeOnlineCourse
from .fee_online_course_payment import FeeOnlineCoursePayment
from .finance_category import FinanceCategory
from .finance_entry import FinanceEntry
from .finance_item import FinanceItem
from .finance_sub_category import FinanceSubCategory
from .instalment_base import InstalmentBase
from .instalment import Instalment
from .module_assessment import ModuleAssessment
from .module_sequence import ModuleSequence
from .module_term import ModuleTerm
from .module_year import ModuleYear
from .moratory import Moratory
from .note import Note
from .online_course_assessment_answer import OnlineCourseAssessmentAnswer
from .online_course_assessment import OnlineCourseAssessment
from .online_course import OnlineCourse
from .online_course_reading import OnlineCourseReading
from .parent import Parent
from .payment_instalment import PaymentInstalment
from .payment import Payment
from .pay_category import PayCategory
from .pay_recursive_item_data import PayRecursiveItemData
from .pay_recursive_item import PayRecursiveItem
from .pay_static_item_data import PayStaticItemData
from .pay_static_item import PayStaticItem
from .school import School
from .sequence import Sequence
from .staff import Staff
from .student_message import StudentMessage
from .student import Student
from .student_move_scan import StudentMoveScan
from .student_parent import StudentParent
from .subject_group import SubjectGroup
from .subject import Subject
from .term import Term
from .yearly_staff import YearlyStaff
from .yearly_student import YearlyStudent

__all__ = [
    "AcademicYear",
    "Assessment",
    "Booking",
    "BookCategory",
    "Book",
    "ClassGroup",
    "ClassRoll",
    "ClassRoom",
    "ContractData",
    "DisciplineAssessment",
    "Discipline",
    "DisciplineSequence",
    "DisciplineTerm",
    "DisciplineYear",
    "FeeCategory",
    "FeeLibrary",
    "FeeLibraryPayment",
    "FeeOnlineCourse",
    "FeeOnlineCoursePayment",
    "FinanceCategory",
    "FinanceEntry",
    "FinanceItem",
    "FinanceSubCategory",
    "InstalmentBase",
    "Instalment",
    "ModuleAssessment",
    "ModuleSequence",
    "ModuleTerm",
    "ModuleYear",
    "Moratory",
    "Note",
    "OnlineCourseAssessmentAnswer",
    "OnlineCourseAssessment",
    "OnlineCourse",
    "OnlineCourseReading",
    "Parent",
    "PaymentInstalment",
    "Payment",
    "PayCategory",
    "PayRecursiveItemData",
    "PayRecursiveItem",
    "PayStaticItemData",
    "PayStaticItem",
    "School",
    "Sequence",
    "Staff",
    "StudentMessage",
    "Student",
    "StudentMoveScan",
    "StudentParent",
    "SubjectGroup",
    "Subject",
    "Term",
    "YearlyStaff",
    "YearlyStudent",
]

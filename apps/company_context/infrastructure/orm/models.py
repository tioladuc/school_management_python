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
]

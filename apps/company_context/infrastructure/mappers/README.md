# Generated Django mappers

Generated from `orm(1).zip`. 55 mapper files were created.

## Conventions
- Each mapper follows the `to_domain(m)` / `to_model(e, m=None)` pattern.
- Domain entity modules are assumed to be `...domain.entities.<entity_snake_case>`.
- Entity class names are derived from ORM class names by removing the `Model` or `Module` suffix.
- Foreign keys are represented in domain entities as scalar `<field>_id` attributes.
- `id` and all declared model fields are passed to the domain entity constructor.
- `id`, `auto_now`, and `auto_now_add` fields are not assigned in `to_model`; Django manages timestamps.
- `ContractModel` and `SubscriptionModel` were excluded as requested.

## Mapper files
- `academic_year_mapper.py` — `AcademicYearModel` → `AcademicYear`
- `assessment_mapper.py` — `AssessmentModel` → `Assessment`
- `booking_mapper.py` — `BookingModel` → `Booking`
- `book_category_mapper.py` — `BookCategoryModel` → `BookCategory`
- `book_mapper.py` — `BookModel` → `Book`
- `class_group_mapper.py` — `ClassGroupModel` → `ClassGroup`
- `class_roll_mapper.py` — `ClassRollModel` → `ClassRoll`
- `class_room_mapper.py` — `ClassRoomModel` → `ClassRoom`
- `contract_data_mapper.py` — `ContractDataModel` → `ContractData`
- `discipline_assessment_mapper.py` — `DisciplineAssessmentModel` → `DisciplineAssessment`
- `discipline_mapper.py` — `DisciplineModel` → `Discipline`
- `discipline_sequence_mapper.py` — `DisciplineSequenceModel` → `DisciplineSequence`
- `discipline_term_mapper.py` — `DisciplineTermModel` → `DisciplineTerm`
- `discipline_year_mapper.py` — `DisciplineYearModel` → `DisciplineYear`
- `fee_category_mapper.py` — `FeeCategoryModel` → `FeeCategory`
- `fee_library_mapper.py` — `FeeLibraryModel` → `FeeLibrary`
- `fee_library_payment_mapper.py` — `FeeLibraryPaymentModel` → `FeeLibraryPayment`
- `fee_online_course_mapper.py` — `FeeOnlineCourseModel` → `FeeOnlineCourse`
- `fee_online_course_payment_mapper.py` — `FeeOnlineCoursePaymentModel` → `FeeOnlineCoursePayment`
- `finance_category_mapper.py` — `FinanceCategoryModel` → `FinanceCategory`
- `finance_entry_mapper.py` — `FinanceEntryModel` → `FinanceEntry`
- `finance_item_mapper.py` — `FinanceItemModel` → `FinanceItem`
- `finance_sub_category_mapper.py` — `FinanceSubCategoryModel` → `FinanceSubCategory`
- `instalment_base_mapper.py` — `InstalmentBaseModel` → `InstalmentBase`
- `instalment_mapper.py` — `InstalmentModel` → `Instalment`
- `module_assessment_mapper.py` — `ModuleAssessmentModel` → `ModuleAssessment`
- `module_sequence_mapper.py` — `ModuleSequenceModel` → `ModuleSequence`
- `module_term_mapper.py` — `ModuleTermModel` → `ModuleTerm`
- `module_year_mapper.py` — `ModuleYearModel` → `ModuleYear`
- `moratory_mapper.py` — `MoratoryModel` → `Moratory`
- `note_mapper.py` — `NoteModel` → `Note`
- `online_course_assessment_answer_mapper.py` — `OnlineCourseAssessmentAnswerModel` → `OnlineCourseAssessmentAnswer`
- `online_course_assessment_mapper.py` — `OnlineCourseAssessmentModel` → `OnlineCourseAssessment`
- `online_course_mapper.py` — `OnlineCourseModel` → `OnlineCourse`
- `online_course_reading_mapper.py` — `OnlineCourseReadingModel` → `OnlineCourseReading`
- `parent_mapper.py` — `ParentModule` → `Parent`
- `payment_instalment_mapper.py` — `PaymentInstalmentModel` → `PaymentInstalment`
- `payment_mapper.py` — `PaymentModel` → `Payment`
- `pay_category_mapper.py` — `PayCategoryModel` → `PayCategory`
- `pay_recursive_item_data_mapper.py` — `PayRecursiveItemData` → `PayRecursiveItemData`
- `pay_recursive_item_mapper.py` — `PayRecursiveItem` → `PayRecursiveItem`
- `pay_static_item_data_mapper.py` — `PayStaticItemData` → `PayStaticItemData`
- `pay_static_item_mapper.py` — `PayStaticItem` → `PayStaticItem`
- `school_mapper.py` — `SchoolModel` → `School`
- `sequence_mapper.py` — `SequenceModel` → `Sequence`
- `staff_mapper.py` — `StaffModel` → `Staff`
- `student_message_mapper.py` — `StudentMessageModel` → `StudentMessage`
- `student_mapper.py` — `StudentModule` → `Student`
- `student_move_scan_mapper.py` — `StudentMoveScanModel` → `StudentMoveScan`
- `student_parent_mapper.py` — `StudentParentModule` → `StudentParent`
- `subject_group_mapper.py` — `SubjectGroupModel` → `SubjectGroup`
- `subject_mapper.py` — `SubjectModel` → `Subject`
- `term_mapper.py` — `TermModel` → `Term`
- `yearly_staff_mapper.py` — `YearlyStaffModel` → `YearlyStaff`
- `yearly_student_mapper.py` — `YearlyStudentModel` → `YearlyStudent`

## Important integration notes
- The ZIP contains ORM model definitions, not domain entity definitions. The generated imports and constructor attributes therefore assume matching domain entities exist.
- `ContractDataModel` is included because only `ContractModel` and `SubscriptionModel` were excluded. Its `contract_id` reference still requires the corresponding contract record/model to exist in the ORM layer.
- If your domain entities use relation objects rather than foreign-key IDs, adjust the corresponding `<field>_id` attributes in both mapper methods.
- Verify entity constructor signatures, optional/null fields, and any custom field conversion rules before integrating.

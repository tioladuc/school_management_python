from django.db import models
from .yearly_student_model import YearlyStudentModel
from .subject_model import SubjectModel
from .assessment_model import AssessmentModel
from .yearly_staff_model import YearlyStaffModel

class NoteModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')
    subject=models.ForeignKey(SubjectModel,on_delete=models.PROTECT,related_name='%(class)s_subjects')
    assessment=models.ForeignKey(AssessmentModel,on_delete=models.PROTECT,related_name='%(class)s_assessments')
    
    mark=models.FloatField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='note'
        constraints=[models.UniqueConstraint(fields=['yearly_student','subject', 'assessment'], name='%(class)s_uq_student_subject_assessment_name')]
    

__all__ = [
    "NoteModel",
]
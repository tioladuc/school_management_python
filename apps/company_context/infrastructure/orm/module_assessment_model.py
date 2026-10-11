from django.db import models
from .assessment_model import AssessmentModel
from .subject_model import SubjectModel
from .yearly_staff_model import YearlyStaffModel

class ModuleAssessmentModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    assessment=models.ForeignKey(AssessmentModel,on_delete=models.PROTECT,related_name='%(class)s_assessments')
    subject=models.ForeignKey(SubjectModel,on_delete=models.PROTECT,related_name='%(class)s_subjects')

    name_fr=models.CharField(max_length=150)
    name_en=models.CharField(max_length=150)
    description_fr=models.TextField(blank=True)
    description_en=models.TextField(blank=True)

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='module_assessment'
        constraints=[models.UniqueConstraint(fields=['assessment', 'subject'], name='%(class)s_uq_assessment_subject_name')]

__all__ = [
    "ModuleAssessmentModel",
]
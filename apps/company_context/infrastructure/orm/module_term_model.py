from django.db import models
from .term_model import TermModel
from .subject_model import SubjectModel
from .yearly_staff_model import YearlyStaffModel

class ModuleTermModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    term=models.ForeignKey(TermModel,on_delete=models.PROTECT,related_name='%(class)s_terms')
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
        db_table='module_term'
        constraints=[models.UniqueConstraint(fields=['term', 'subject'], name='%(class)s_uq_term_subject_name')]

__all__ = [
    "ModuleTermModel",
]
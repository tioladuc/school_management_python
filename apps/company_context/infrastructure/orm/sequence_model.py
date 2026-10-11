from django.db import models
from .term_model import TermModel
from .yearly_staff_model import YearlyStaffModel

class SequenceModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    term=models.ForeignKey(TermModel,on_delete=models.PROTECT,related_name='%(class)s_terms')

    name_fr=models.CharField(max_length=150)
    name_en=models.CharField(max_length=150)
    description_fr=models.TextField(blank=True)
    description_en=models.TextField(blank=True)
    coeficient=models.IntegerField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='sequence'
        constraints=[models.UniqueConstraint(fields=['term', 'name_fr', 'name_en'], name='%(class)s_uq_sequence_name')]

__all__ = [
    "SequenceModel",
]
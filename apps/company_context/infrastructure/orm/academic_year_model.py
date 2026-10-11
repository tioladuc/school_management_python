from django.db import models
from .school_model import SchoolModel

class AcademicYearModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    school=models.ForeignKey(SchoolModel,on_delete=models.PROTECT,related_name='%(class)s_schools')

    year=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='academic_year'
        constraints=[models.UniqueConstraint(fields=['school', 'year'], name='%(class)s_uq_school_year')]
    

__all__ = [
    "AcademicYearModel",
]
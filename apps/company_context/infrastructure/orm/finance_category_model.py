from django.db import models
from .yearly_staff_model import YearlyStaffModel
from .academic_year_model import AcademicYearModel

class FinanceCategoryModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    academic_year=models.ForeignKey(AcademicYearModel,on_delete=models.PROTECT,related_name='%(class)s_academic_years')
    
    code=models.CharField(max_length=50, unique=True)
    name_fr=models.CharField(max_length=50)
    name_en=models.CharField(max_length=50)
    description_fr= models.TextField()
    description_en= models.TextField()
    initial_amount=models.FloatField()
    current_amount=models.FloatField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='finance_category'
    
__all__ = [
    "FinanceCategoryModel",
]
from django.db import models
from .academic_year_model import AcademicYearModel

class PayCategoryModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    academic_year=models.ForeignKey(AcademicYearModel,on_delete=models.PROTECT,related_name='%(class)s_academic_years')

    code=models.CharField(max_length=50, unique=True)
    name_fr=models.CharField(max_length=50)
    name_en=models.CharField(max_length=50)
    description_fr= models.TextField()
    description_en= models.TextField()
    order=models.IntegerField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='pay_category'
    

__all__ = [
    "PayCategoryModel",
]
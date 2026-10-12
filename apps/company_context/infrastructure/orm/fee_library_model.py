from django.db import models
from .fee_category_model import FeeCategoryModel
from .academic_year_model import AcademicYearModel
from .yearly_staff_model import YearlyStaffModel

class FeeLibraryModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    fee_category=models.ForeignKey(FeeCategoryModel,on_delete=models.PROTECT,related_name='%(class)s_fee_categorys')
    academic_year=models.ForeignKey(AcademicYearModel,on_delete=models.PROTECT,related_name='%(class)s_academic_years')

    name_fr=models.CharField(max_length=150)
    name_en=models.CharField(max_length=150)
    description_fr=models.TextField(blank=True)
    description_en=models.TextField(blank=True)
    amount=models.FloatField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')
    
    class Meta:
        db_table='fee_library'
    

__all__ = [
    "FeeLibraryModel",
]
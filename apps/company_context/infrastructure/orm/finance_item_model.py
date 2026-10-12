from django.db import models
from .finance_subcategory_model import FinanceSubCategoryModel
from .yearly_staff_model import YearlyStaffModel

class FinanceItemModel(models.Model):
    TYPE_CHOICES=[('INCOME','Income'),('EXPENSE','Expense')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    finance_subcategory=models.ForeignKey(FinanceSubCategoryModel,on_delete=models.PROTECT,related_name='%(class)s_finance_subcategory')
    
    code=models.CharField(max_length=50, unique=True)
    name_fr=models.CharField(max_length=50)
    name_en=models.CharField(max_length=50)
    description_fr= models.TextField()
    description_en= models.TextField()
    initial_amount=models.FloatField()
    current_amount=models.FloatField()

    finance_type=models.CharField(max_length=20, choices=TYPE_CHOICES, default='INCOME')
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='finance_item'
    
__all__ = [
    "FinanceItemModel",
]
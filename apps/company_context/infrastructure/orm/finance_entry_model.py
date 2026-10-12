from django.db import models
from .finance_item_model import FinanceItemModel
from .yearly_staff_model import YearlyStaffModel

class FinanceEntryModel(models.Model):
    TYPE_CHOICES=[('INCOME','Income'),('EXPENSE','Expense')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    finance_item=models.ForeignKey(FinanceItemModel,on_delete=models.PROTECT,related_name='%(class)s_finance_item')
        
    amount=models.FloatField()
    deposit_date=models.DateTimeField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='finance_entry'
    
__all__ = [
    "FinanceEntryModel",
]
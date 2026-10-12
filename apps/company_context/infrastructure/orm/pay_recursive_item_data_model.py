from django.db import models
from .pay_recursive_item_model import PayRecursiveItem
from .yearly_staff_model import YearlyStaffModel

class PayRecursiveItemData(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    pay_recursive_item=models.ForeignKey(PayRecursiveItem,on_delete=models.PROTECT,related_name='%(class)s_pay_recursive_items')
    yearly_staff=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_staffs')
    
    start_period= models.DateField()
    end_period= models.DateField()
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='pay_recursive_item_data'
    

__all__ = [
    "PayRecursiveItemData",
]
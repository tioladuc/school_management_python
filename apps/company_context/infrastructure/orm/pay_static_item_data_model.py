from django.db import models
from .pay_static_item_model import PayStaticItem
from .yearly_staff_model import YearlyStaffModel

class PayStaticItemData(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    pay_static_item=models.ForeignKey(PayStaticItem,on_delete=models.PROTECT,related_name='%(class)s_pay_static_items')
    yearly_staff=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_staffs')
    
    date_payment= models.DateField()
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='pay_static_item_data'
    

__all__ = [
    "PayStaticItemData",
]
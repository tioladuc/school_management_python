from django.db import models
from .payment_model import PaymentModel
from .instalment_base_model import InstalmentBaseModel
from .yearly_staff_model import YearlyStaffModel

class PaymentInstalmentModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    payment=models.ForeignKey(PaymentModel,on_delete=models.PROTECT,related_name='%(class)s_payments')
    base_instalment=models.ForeignKey(InstalmentBaseModel,on_delete=models.PROTECT,related_name='%(class)s_base_instalments')

    description= models.CharField(max_length=100,)
    amount=models.IntegerField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')
    
    class Meta:
        db_table='payment_instalment'
        constraints=[models.UniqueConstraint(fields=['payment', 'base_instalment'], name='%(class)s_uq_payment_baseinstalment_name')]
    

__all__ = [
    "PaymentInstalmentModel",
]
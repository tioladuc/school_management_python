from django.db import models
from .company_model import CompanyModel

class SubscriptionModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('CANCELLED','Cancelled')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='subscriptions')
    plan_code=models.CharField(max_length=80)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='ACTIVE')
    class Meta: db_table='subscription'

__all__ = [
    "SubscriptionModel",
]
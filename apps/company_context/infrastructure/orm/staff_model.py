from django.db import models
from .company_model import CompanyModel

class StaffModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='staff')
    staff_number=models.CharField(max_length=80)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=50,blank=True)
    position=models.CharField(max_length=150,blank=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='staff'
        constraints=[models.UniqueConstraint(fields=['company','staff_number'],name='uq_staff_company_number')]

__all__ = [
    "StaffModel",
]
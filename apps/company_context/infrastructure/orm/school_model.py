from django.db import models
from .company_model import CompanyModel

class SchoolModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='schools')
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=250)
    city=models.CharField(max_length=150)
    country=models.CharField(max_length=100)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='school'
        constraints=[models.UniqueConstraint(fields=['company','code'],name='uq_school_company_code')]

__all__ = [
    "SchoolModel",
]
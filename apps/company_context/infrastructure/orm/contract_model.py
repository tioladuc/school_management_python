from django.db import models
from .company_model import CompanyModel

class ContractModel(models.Model):
    STATUS_CHOICES=[('DRAFT','Draft'),('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='contracts')
    signature_date=models.DateField()
    company_setup_price=models.DecimalField(max_digits=14,decimal_places=2)
    school_setup_price=models.DecimalField(max_digits=14,decimal_places=2)
    academic_year_renewal_price=models.DecimalField(max_digits=14,decimal_places=2)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='DRAFT')
    currency=models.CharField(max_length=3,default='CAD')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: db_table='contract'

__all__ = [
    "ContractModel",
]
from django.db import models
from .contract_model import ContractModel

class ContractDataModel(models.Model):
    TRANSACTION_TYPES=[('COMPANY_CREATION','Company creation'),('SCHOOL_CREATION','School creation'),('ACADEMIC_YEAR_RENEWAL','Academic year renewal'),('CUSTOM_FEE','Custom fee'),('DISCOUNT','Discount'),('CREDIT_NOTE','Credit note')]
    STATUS_CHOICES = [
            ("ACTIVE", "Active"),
            ("SUSPENDED", "Suspended"),
            ("TERMINATED", "Terminated"),
        ]
    contract=models.ForeignKey(ContractModel,on_delete=models.PROTECT,related_name='contracts')
    transaction_type=models.CharField(max_length=40,choices=TRANSACTION_TYPES)
    transaction_date=models.DateField()
    quantity=models.DecimalField(max_digits=14,decimal_places=3)
    unit_price=models.DecimalField(max_digits=14,decimal_places=2)
    total_amount=models.DecimalField(max_digits=14,decimal_places=2)
    description=models.TextField(blank=True)

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta: db_table='contract_data'

__all__ = [
    "ContractDataModel",
]

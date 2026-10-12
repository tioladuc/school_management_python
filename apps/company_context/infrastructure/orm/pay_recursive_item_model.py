from django.db import models
from .pay_category_model import PayCategoryModel
from .yearly_staff_model import YearlyStaffModel

class PayRecursiveItem(models.Model):
    TYPE_CHOICES=[('INPUT','Input'),('OUTPUT','Output')]
    CALCULATION_CHOICES=[('PERCENTAGE','Percentage'),('FIXE','Fixe')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    pay_category=models.ForeignKey(PayCategoryModel,on_delete=models.PROTECT,related_name='%(class)s_pay_categories')

    code=models.CharField(max_length=50, unique=True)
    name_fr=models.CharField(max_length=50)
    name_en=models.CharField(max_length=50)
    description_fr= models.TextField()
    description_en= models.TextField()
    order=models.IntegerField()

    type_choice=models.CharField(max_length=20, choices=TYPE_CHOICES, default='INPUT')
    calculation_choice=models.CharField(max_length=20, choices=CALCULATION_CHOICES, default='PERCENTAGE')
    value=models.FloatField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')
    
    class Meta:
        db_table='pay_recursive_item'
    

__all__ = [
    "PayRecursiveItem",
]
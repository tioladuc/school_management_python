from django.db import models
from .academic_year_model import AcademicYearModel
from .staff_model import StaffModel

class YearlyStaffModel(models.Model):
    PROFILE_CHOICES=[('TEACHER','Teacher'),('ACCOUNTANT','Account'),('SECRETARY','Secretary'),('ADMINISTRATOR','Administrator'),('SUPER_ADMINISTRATOR','Super_Administrator')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    PAYMENT_TYPE_CHOICES=[('HOURLY','Hourly'),('FIXE','Fixe')]
    academic_year=models.ForeignKey(AcademicYearModel,on_delete=models.PROTECT,related_name='%(class)s_academic_years')
    staff=models.ForeignKey(StaffModel,on_delete=models.PROTECT,related_name='%(class)s_staffs')

    profile=models.CharField(max_length=50, choices=PROFILE_CHOICES, default='TEACHER')
    payment_type=models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, default='HOURLY')

    fixed_amount=models.FloatField()
    hour_amount=models.FloatField()        
    hour_sup_15_amount=models.FloatField()        
    hour_sup_20_amount=models.FloatField()        
    hour_sup_30_amount=models.FloatField()        
    hour_sup_40_amount=models.FloatField()        
    hour_sup_50_amount=models.FloatField()        
    day_amount=models.FloatField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='yearly_staff'
        constraints=[models.UniqueConstraint(fields=['academic_year', 'staff'], name='%(class)s_uq_yearly_staff_name')]
    
__all__ = [
    "YearlyStaffModel",
]
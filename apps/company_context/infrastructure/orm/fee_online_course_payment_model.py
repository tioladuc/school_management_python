from django.db import models
from .fee_online_course_model import FeeOnlineCourseModel
from .yearly_student_model import YearlyStudentModel
from .yearly_staff_model import YearlyStaffModel

class FeeOnlineCoursePaymentModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    fee_online_course=models.ForeignKey(FeeOnlineCourseModel,on_delete=models.PROTECT,related_name='%(class)s_fee_online_courses')
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')

    paid_by=models.CharField(max_length=150)
    paid_on=models.DateField(max_length=150)
    deposited_amount=models.FloatField(blank=True)

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')
    
    class Meta:
        db_table='fee_online_course_payment'
    

__all__ = [
    "FeeOnlineCoursePaymentModel",
]
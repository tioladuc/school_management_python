from django.db import models
from .yearly_student_model import YearlyStudentModel
from .yearly_staff_model import YearlyStaffModel

class PaymentModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')
    staff=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_staffs')

    deposited_by= models.CharField(max_length=50,)
    amount=models.IntegerField()
    payment_date=models.DateTimeField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='payment'
        constraints=[models.UniqueConstraint(fields=['yearly_student', 'payment_date'], name='%(class)s_uq_yearlystudent_payment')]
    

__all__ = [
    "PaymentModel",
]
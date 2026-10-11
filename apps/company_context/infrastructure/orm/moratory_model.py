from django.db import models
from .yearly_student_model import YearlyStudentModel
from .yearly_staff_model import YearlyStaffModel

class MoratoryModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')
    
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='moratory'
        constraints=[models.UniqueConstraint(fields=['yearly_student', 'start_date', 'end_date'], name='%(class)s_uq_yearlystudent_academicyear_name')]
    
__all__ = [
    "MoratoryModel",
]
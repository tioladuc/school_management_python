from django.db import models
from .yearly_student_model import YearlyStudentModel
from .yearly_staff_model import YearlyStaffModel

class DisciplineModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')

    justified_absence = models.IntegerField()
    unjustified_absence = models.IntegerField()
    lateness = models.IntegerField()
    reserve = models.IntegerField()
    notice = models.IntegerField()
    blame = models.IntegerField()
    exclusion = models.IntegerField()

    description = models.TextField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')
    
    class Meta:
        db_table='discipline'
    

__all__ = [
    "DisciplineModel",
]
from django.db import models
from .online_course_model import OnlineCourseModel
from .yearly_student_model import YearlyStudentModel
from .yearly_staff_model import YearlyStaffModel

class OnlineCourseReadingModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    online_course=models.ForeignKey(OnlineCourseModel,on_delete=models.PROTECT,related_name='%(class)s_online_courses')
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')

    reading_date=models.DateTimeField(max_length=150)

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')
    
    class Meta:
        db_table='online_course_reading'
    

__all__ = [
    "OnlineCourseReadingModel",
]
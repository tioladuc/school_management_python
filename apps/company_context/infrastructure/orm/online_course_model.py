from django.db import models
from .subject_model import SubjectModel
from .yearly_staff_model import YearlyStaffModel
from .yearly_staff_model import YearlyStaffModel

class OnlineCourseModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    subject=models.ForeignKey(SubjectModel,on_delete=models.PROTECT,related_name='%(class)s_subjects')
    yearly_staff=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_staffs')

    name_fr=models.CharField(max_length=150)
    name_en=models.CharField(max_length=150)
    description_fr=models.TextField(blank=True)
    description_en=models.TextField(blank=True)
    file_path=models.CharField(max_length=150)

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')
    
    class Meta:
        db_table='online_course'
    

__all__ = [
    "OnlineCourseModel",
]
from django.db import models
from .yearly_student_model import YearlyStudentModel
from .subject_model import SubjectModel
from .yearly_staff_model import YearlyStaffModel

class StudentMessageModel(models.Model):
    CATEGORY_CHOICES=[('GENERAL','General'),('FINANCE','Finance'),('DISCIPLINE','Discipline'),('MARK','Mark')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')
    subject=models.ForeignKey(SubjectModel,on_delete=models.PROTECT,related_name='%(class)s_subjects')
        
    start_period=models.DateTimeField()
    end_period=models.DateTimeField()
    subject_fr=models.CharField(max_length=100)
    subject_en=models.CharField(max_length=100)
    content_fr=models.CharField(max_length=100)
    content_en=models.CharField(max_length=100)
    teacher=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_teachers')

    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='ACTIVE')
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='student_message'
    
__all__ = [
    "StudentMessageModel",
]
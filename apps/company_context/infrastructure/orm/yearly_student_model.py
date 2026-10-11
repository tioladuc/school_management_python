from django.db import models
from .academic_year_model import AcademicYearModel
from .student_module import StudentModule
from .class_room_model import ClassRoomModel

class YearlyStudentModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    student=models.ForeignKey(StudentModule,on_delete=models.PROTECT,related_name='%(class)s_students')
    academic_year=models.ForeignKey(AcademicYearModel,on_delete=models.PROTECT,related_name='%(class)s_academic_years')
    class_room=models.ForeignKey(ClassRoomModel,on_delete=models.PROTECT,related_name='%(class)s_class_rooms')
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='yearly_student'
        constraints=[models.UniqueConstraint(fields=['student','academic_year', 'class_room'], name='%(class)s_uq_student_academicyear_classroom_name')]
    

__all__ = [
    "YearlyStudentModel",
]
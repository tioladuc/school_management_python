from django.db import models
from .student_module import StudentModule
from .parent_model import ParentModule

class StudentParentModule(models.Model):
    RELATION_CHOICES=[('FATHER','Father'),('MOTHER','Mother'),('TUTOR','Tutor')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    student=models.ForeignKey(StudentModule,on_delete=models.PROTECT,related_name='students')
    parent=models.ForeignKey(ParentModule,on_delete=models.PROTECT,related_name='parentss')
    
    relation=models.CharField(max_length=20, choices=RELATION_CHOICES, default='FATHER')

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='student_parent'
        constraints=[models.UniqueConstraint(fields=['student','parent'], name='uq_student_parent_name')]
    

__all__ = [
    "StudentParentModule",
]
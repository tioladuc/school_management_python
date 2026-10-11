from django.db import models
from .term_model import TermModel
from .yearly_student_model import YearlyStudentModel
from .term_model import TermModel
from .yearly_staff_model import YearlyStaffModel

class DisciplineTermModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')
    term=models.ForeignKey(TermModel,on_delete=models.PROTECT,related_name='%(class)s_terms')

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
        db_table='discipline_term'
        constraints=[models.UniqueConstraint(fields=['yearly_student', 'term'], name='%(class)s_uq_yearly_student_term_name')]
    

__all__ = [
    "DisciplineTermModel",
]
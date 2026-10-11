from django.db import models
from .class_room_model import ClassRoomModel
from .subject_group_model import SubjectGroupModel
from .yearly_staff_model import YearlyStaffModel

class SubjectModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    class_room=models.ForeignKey(ClassRoomModel,on_delete=models.PROTECT,related_name='%(class)s_class_rooms')
    subject_group=models.ForeignKey(SubjectGroupModel,on_delete=models.PROTECT,related_name='%(class)s_subject_groups')
    yearly_staff=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_staffs')

    name_fr=models.CharField(max_length=150)
    name_en=models.CharField(max_length=150)
    description_fr=models.TextField(blank=True)
    description_en=models.TextField(blank=True)    
    coeficient=models.IntegerField()
    order=models.IntegerField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='subject'
        constraints=[models.UniqueConstraint(fields=['class_room', 'subject_group', 'yearly_staff'], name='%(class)s_uq_classroom_subject_staff_name')]
    
__all__ = [
    "SubjectModel",
]
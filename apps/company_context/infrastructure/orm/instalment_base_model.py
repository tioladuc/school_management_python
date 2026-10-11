from django.db import models
from .instalment_model import InstalmentModel
from .class_room_model import ClassRoomModel
from .yearly_staff_model import YearlyStaffModel

class InstalmentBaseModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    instalment=models.ForeignKey(InstalmentModel,on_delete=models.PROTECT,related_name='%(class)s_instalments')
    class_room=models.ForeignKey(ClassRoomModel,on_delete=models.PROTECT,related_name='%(class)s_class_rooms')

    amount=models.IntegerField(blank=True)

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='instalment_base'
        constraints=[models.UniqueConstraint(fields=['instalment', 'class_room'], name='%(class)s_uq_instalment_classroom_name')]
    

__all__ = [
    "InstalmentBaseModel",
]
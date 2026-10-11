from django.db import models

class StaffModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]

    staff_number=models.CharField(max_length=80, unique=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=50,blank=True)
    position=models.CharField(max_length=150,blank=True)
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='staff'

__all__ = [
    "StaffModel",
]
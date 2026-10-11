from django.db import models

class ParentModule(models.Model):
    GENDER_CHOICES=[('MALE','Male'),('FEMALE','Female')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    
    code=models.CharField(max_length=20, unique=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    profession=models.CharField(max_length=150)
    gender=models.CharField(max_length=20, choices=GENDER_CHOICES, default='MALE')

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='parent'
    

__all__ = [
    "ParentModule",
]
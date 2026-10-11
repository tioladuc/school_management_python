from django.db import models

class SchoolModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]

    code=models.CharField(max_length=50, unique=True)
    name_fr=models.CharField(max_length=250)
    name_en=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    autorization=models.CharField(max_length=250)
    founder=models.CharField(max_length=250)
    principal=models.CharField(max_length=250)
    city=models.CharField(max_length=150)
    country=models.CharField(max_length=100)
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='school'
        constraints=[models.UniqueConstraint(fields=['code'],name='uq_school_code')]

__all__ = [
    "SchoolModel",
]
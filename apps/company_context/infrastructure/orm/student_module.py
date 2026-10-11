from django.db import models

class StudentModule(models.Model):
    GENDER_CHOICES=[('MALE','Male'),('FEMALE','Female')]
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]

    code=models.CharField(max_length=20, unique=True)
    gov_matricule=models.CharField(max_length=50, unique=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    born_at=models.CharField(max_length=150)
    born_on=models.DateField()
    gender=models.CharField(max_length=20, choices=GENDER_CHOICES, default='MALE')
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='student'
    

__all__ = [
    "StudentModule",
]
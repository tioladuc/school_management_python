from django.db import models
from .school_model import SchoolModel

class BookCategoryModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    school=models.ForeignKey(SchoolModel,on_delete=models.PROTECT,related_name='%(class)s_schools')

    name_fr=models.CharField(max_length=150)
    name_en=models.CharField(max_length=150)
    description_fr=models.TextField(blank=True)
    description_en=models.TextField(blank=True)
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='book_category'
        constraints = [
            models.UniqueConstraint(
                fields=['school', 'name_fr', 'name_en'],
                name='uq_book_category_school_names'
            )
        ]

__all__ = [
    "BookCategoryModel",
]
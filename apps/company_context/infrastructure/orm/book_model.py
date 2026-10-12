from django.db import models
from .book_category_model import BookCategoryModel

class BookModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    book_category=models.ForeignKey(BookCategoryModel,on_delete=models.PROTECT,related_name='%(class)s_book_categorys')

    name_fr=models.CharField(max_length=150)
    name_en=models.CharField(max_length=150)
    description_fr=models.TextField(blank=True)
    description_en=models.TextField(blank=True)
    author=models.CharField(max_length=150)
    second_name_fr=models.CharField(max_length=150)
    second_name_en=models.CharField(max_length=150)
    published_date=models.CharField(max_length=150)
    published_by=models.CharField(max_length=150)
    illustrated_by=models.CharField(max_length=150)
    keywords=models.CharField(max_length=150)
    quantity=models.IntegerField()
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='book'
        constraints=[models.UniqueConstraint(fields=['sequence', 'name_fr', 'name_en'], name='%(class)s_uq_assessment_name')]

__all__ = [
    "BookModel",
]
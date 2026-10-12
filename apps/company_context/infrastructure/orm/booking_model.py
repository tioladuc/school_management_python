from django.db import models
from .book_model import BookModel
from .yearly_student_model import YearlyStudentModel

class BookingModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('NOT_RETURNED','Not_returned'),('RETURNED','Returned')]
    book=models.ForeignKey(BookModel,on_delete=models.PROTECT,related_name='%(class)s_books')
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')

    booking_date=models.DateField()
    return_date=models.DateField()
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='booking'
        constraints=[models.UniqueConstraint(fields=['sequence', 'name_fr', 'name_en'], name='%(class)s_uq_assessment_name')]

__all__ = [
    "BookingModel",
]
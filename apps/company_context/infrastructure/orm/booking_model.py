from django.db import models
from .book_model import BookModel
from .yearly_student_model import YearlyStudentModel
from .yearly_staff_model import YearlyStaffModel

class BookingModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('NOT_RETURNED','Not_returned'),('RETURNED','Returned')]
    book=models.ForeignKey(BookModel,on_delete=models.PROTECT,related_name='%(class)s_books')
    yearly_student=models.ForeignKey(YearlyStudentModel,on_delete=models.PROTECT,related_name='%(class)s_yearly_students')

    booking_date=models.DateField()
    return_date=models.DateField()
    
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_created_bys')
    update_by=models.ForeignKey(YearlyStaffModel,on_delete=models.PROTECT,related_name='%(class)s_updated_bys')

    class Meta:
        db_table='booking'
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'yearly_student', 'booking_date'],
                name='uq_booking_book_student_date'
            )
        ]

__all__ = [
    "BookingModel",
]
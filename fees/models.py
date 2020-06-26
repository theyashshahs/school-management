from django.db import models
from student.models import Student
import datetime

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fees = models.IntegerField()
    dateofpayment = models.DateField(default=datetime.date.today)
    paymentreceipt = models.URLField(blank=True)

    def __str__(self):
        return f'{self.student}'

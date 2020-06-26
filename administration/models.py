from django.db import models
from teacher.models import Teacher
from student.models import Student
import datetime

class Class(models.Model):
    class_id = models.CharField(primary_key=True, max_length=10)
    class_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.class_id)


class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fees = models.IntegerField()
    dateofpayment = models.DateField(default=datetime.date.today)
    paymentreceipt = models.URLField(blank=True)

    def __str__(self):
        return self.student

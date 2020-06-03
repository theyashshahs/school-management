from django.db import models
from teacher.models import Teacher
from student.models import Student

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course_id)


class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fees = models.IntegerField()
    dateofpayment = models.DateField()
    paymentreceipt = models.FileField(upload_to="receipt/", blank=True)

    def __str__(self):
        return self.student

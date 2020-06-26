from django.db import models
from teacher.models import Assignment
from administration.models import Class

class Student(models.Model):
    roll_number = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    profilepic = models.URLField(blank=True)
    attendance = models.DecimalField(max_digits=5, decimal_places=2)
    class_name = models.ForeignKey(Class, default=1201, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.roll_number + ' - ' + self.first_name + ' ' + self.last_name


class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    answer = models.URLField(blank=True)

    def __str__(self):
        return f'{self.student} {self.assignment}'
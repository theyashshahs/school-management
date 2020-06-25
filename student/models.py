from django.db import models
from teacher.models import Assignment

class Student(models.Model):
    roll_number = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    profilepic = models.URLField(blank=True)

    def __str__(self):
        return self.roll_number + ' - ' + self.first_name + ' ' + self.last_name


class AssignmentAnswer(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    answer = models.URLField(blank=True)

    def __str__(self):
        return str(self.assignment)
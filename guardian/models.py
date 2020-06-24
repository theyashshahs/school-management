from django.db import models
from student.models import Student

class Guardian(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    


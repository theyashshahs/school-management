from django.db import models
# from administration.models import Class
import datetime

class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profilepic = models.URLField(blank=True)
    # class_id = Class._meta.get_field('class_id')

    def __str__(self):
        return str(self.teacher_id) + ' ' + self.first_name + ' ' + self.last_name


class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    serial_number = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length=100)
    due_date = models.DateField(default=datetime.date.today)
    upload = models.URLField(blank=False)

    def __str__(self):
        return str(self.heading)
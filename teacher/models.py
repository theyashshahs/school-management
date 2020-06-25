from django.db import models
import datetime
class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profilepic = models.URLField(blank=True)

    def __str__(self):
        return str(self.teacher_id) + ' ' + self.first_name + ' ' + self.last_name


class Assignment(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length=100)
    due_date = models.DateField(default=datetime.date.today)
    upload = models.URLField(blank=False)


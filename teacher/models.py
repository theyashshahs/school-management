from django.db import models

class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='profilepics/teacher/', blank=True)

    def __str__(self):
        return str(self.teacher_id) + ' ' + self.first_name + ' ' + self.last_name


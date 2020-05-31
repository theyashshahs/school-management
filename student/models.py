from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(primary_key=True, max_length=10)
    dob = models.DateField()
    profilepic = models.ImageField(upload_to='profilepics/student/', blank=True)

    def __str__(self):
        return self.roll_number + ' - ' + self.first_name + ' ' + self.last_name

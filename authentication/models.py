from django.db import models

class Auth(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.username} {self.role}'

from django.db import models

class Auth(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

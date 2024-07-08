from django.db import models
from django.contrib.auth.models import User

class task(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    deadline = models.DateField()

from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

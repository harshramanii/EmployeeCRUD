from django.db import models

# Create your models here.


class Employee(models.Model):
    nm = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)

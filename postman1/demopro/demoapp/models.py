from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    empid = models.TextField(max_length=100)
    company = models.CharField(max_length=100)
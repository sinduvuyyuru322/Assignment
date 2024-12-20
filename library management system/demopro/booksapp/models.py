from django.db import models

# Create your models here.
class Books(models.Model):
    Title = models.CharField(max_length=200)
    Auth = models.CharField(max_length=100)
    Year = models.IntegerField()
    Genre = models.CharField(max_length=100)


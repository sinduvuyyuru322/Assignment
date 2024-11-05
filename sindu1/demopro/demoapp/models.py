from django.db import models

# Create your models here.
class Delivary_address(models.Model):
    emailid = models.EmailField(default='emailid@example.com')
    passward = models.TextField(max_length=10)
    
    
class address(models.Model):
    emailid = models.EmailField(default='emailid@example.com')
    passward = models.TextField(max_length=10)
    conform = models.TextField(max_length=10)
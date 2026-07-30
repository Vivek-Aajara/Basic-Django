from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.IntegerField()
    age = models.IntegerField()
    department = models.CharField(max_length=100)

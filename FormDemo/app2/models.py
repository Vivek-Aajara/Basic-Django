from django.db import models

# Create your models here.
class Person2(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=3, choices=Gender, default=Gender.MALE)
    phone = models.CharField(max_length=100)

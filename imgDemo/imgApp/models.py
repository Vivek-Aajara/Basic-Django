# Create your models here.
from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female")
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default="Male")
    img = models.ImageField(upload_to="img/")
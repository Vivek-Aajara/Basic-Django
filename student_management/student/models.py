from django.db import models


class Student(models.Model):
    YEAR_CHOICES = [
        (1, "1st Year"),
        (2, "2nd Year"),
        (3, "3rd Year"),
        (4, "4th Year"),
    ]

    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    year = models.IntegerField(choices=YEAR_CHOICES, default=1)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

    class Meta:
        ordering = ["roll_no"]

from django.db import models


class Professor(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)

class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField(default=3)
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="subjects"
    )



from django.shortcuts import render
from .models import Person

def img(request):
    persons = Person.objects.all()
    return render(request, "img.html", {"persons": persons})
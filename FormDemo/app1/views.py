from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    if request.method == "POST":
        n = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        Person.objects.create(name=n,email=email,password=password,phone=phone,gender=gender)

    return render(request,'index.html')
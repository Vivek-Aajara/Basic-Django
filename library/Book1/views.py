from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
# Create your views here.

def book1(request):
    return render(request,'Book1.html')

def page1(request):
    t = loader.get_template('Book1Page1.html')
    return HttpResponse(t.render())

def page2(request):
    return render(request,'Book1Page2.html')
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
# Create your views here.

def book2(request):
   return render(request,'Book2.html')

def page1(request):
    t = loader.get_template('Book2Page1.html')
    return HttpResponse(t.render())

def page2(request):
    return render(request,'Book2Page2.html')
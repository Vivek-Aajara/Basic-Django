from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
# Create your views here.

def book3(request):
    return render(request,'Book3.html')
def page1(request):
    t = loader.get_template('Book3Page1.html')
    return HttpResponse(t.render())

def page2(request):
    return render(request,'Book3Page2.html')
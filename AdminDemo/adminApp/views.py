
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def admin(request): 
    t = loader.get_template('Admin.html')
    return HttpResponse(t.render())
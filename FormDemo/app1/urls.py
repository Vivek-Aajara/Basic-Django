from django.contrib import admin
from django.urls import path,include

import app1
from app1 import views

urlpatterns = [
    path('',views.index,name='index')
]

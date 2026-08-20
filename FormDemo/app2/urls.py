from django.contrib import admin
from django.urls import path,include

import app2
from app2 import views

urlpatterns = [
    path('',views.formdemo,name='formdemo'),
]

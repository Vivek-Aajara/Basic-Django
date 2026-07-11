from django.contrib import admin
from django.urls import path,include

import Book1
from Book3 import views

urlpatterns = [
    path('',views.book3,name='book3'),
    path('page1/',views.page1,name='page1'),
    path('page2/',views.page2,name='page2'),
]

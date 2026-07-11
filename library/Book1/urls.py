from django.contrib import admin
from django.urls import path,include

import Book1
from Book1 import views

urlpatterns = [

    path('',views.book1,name='book1'),

    path('page1/',views.page1,name='page1'),

    path('page2/',views.page2,name='page2'),
]

from django.urls import path
from . import views

app_name = "professor"

urlpatterns = [
    path("", views.professor_list, name="list"),
]
